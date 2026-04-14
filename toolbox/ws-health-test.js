const { spawn } = require('child_process');
const http = require('http');
const fs = require('fs');
const WebSocket = require('ws');

const chrome = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';
const userData = 'C:\\Users\\marco\\.openclaw\\browser\\ws-health-node';

try { fs.rmSync(userData, { recursive: true, force: true }); } catch {}

const args = [
  '--remote-debugging-port=18891',
  `--user-data-dir=${userData}`,
  '--no-first-run',
  '--no-default-browser-check',
  '--disable-sync',
  '--disable-background-networking',
  '--disable-component-update',
  '--disable-features=Translate,MediaRouter',
  '--disable-session-crashed-bubble',
  '--hide-crash-restore-bubble',
  '--password-store=basic',
  'about:blank'
];

function sleep(ms) {
  return new Promise(r => setTimeout(r, ms));
}

function getJson(url) {
  return new Promise((resolve, reject) => {
    http.get(url, res => {
      let data = '';
      res.on('data', c => data += c);
      res.on('end', () => {
        try { resolve(JSON.parse(data)); }
        catch (e) { reject(e); }
      });
    }).on('error', reject);
  });
}

(async () => {
  const proc = spawn(chrome, args, { stdio: ['ignore', 'ignore', 'pipe'] });
  console.log('pid', proc.pid);

  let version = null;
  for (let i = 0; i < 30; i++) {
    try {
      version = await getJson('http://127.0.0.1:18891/json/version');
      console.log('HTTP_OK', version.webSocketDebuggerUrl);
      break;
    } catch (e) {
      console.log('wait-http', i + 1, e.message);
      await sleep(200);
    }
  }

  if (version && version.webSocketDebuggerUrl) {
    let ok = false;
    for (let i = 0; i < 20; i++) {
      try {
        const msg = await new Promise((resolve, reject) => {
          const ws = new WebSocket(version.webSocketDebuggerUrl, { handshakeTimeout: 800 });
          let settled = false;
          const finish = (err, val) => {
            if (settled) return;
            settled = true;
            try { ws.close(); } catch {}
            err ? reject(err) : resolve(val);
          };
          const t = setTimeout(() => finish(new Error('timeout')), 825);
          ws.on('open', () => {
            try {
              ws.send(JSON.stringify({ id: 1, method: 'Browser.getVersion' }));
            } catch (e) {
              clearTimeout(t);
              finish(e);
            }
          });
          ws.on('message', raw => {
            try {
              const parsed = JSON.parse(raw.toString());
              if (parsed && parsed.id === 1) {
                clearTimeout(t);
                finish(null, parsed);
              }
            } catch {}
          });
          ws.on('error', e => {
            clearTimeout(t);
            finish(e);
          });
        });
        console.log('WS_OK', JSON.stringify(msg).slice(0, 200));
        ok = true;
        break;
      } catch (e) {
        console.log('wait-ws', i + 1, e.message);
        await sleep(200);
      }
    }
    console.log('WS_FINAL', ok);
  }

  console.log('alive', proc.exitCode === null);
  try { proc.kill('SIGTERM'); } catch {}
  setTimeout(() => {
    try { proc.kill('SIGKILL'); } catch {}
  }, 1000);
})();
