import json
import urllib.request
import urllib.error

cfg = json.load(open(r'C:\Users\marco\.openclaw\openclaw.json', 'r', encoding='utf-8'))
token = cfg['gateway']['auth']['token']
headers = {'Authorization': 'Bearer ' + token, 'Content-Type': 'application/json'}
base = 'http://127.0.0.1:18791/'
checks = [
    ('?profile=openclaw', 'GET', None),
    ('profiles', 'GET', None),
    ('start?profile=openclaw', 'POST', b'{}'),
    ('?profile=openclaw', 'GET', None),
    ('tabs?profile=openclaw', 'GET', None),
    ('tabs/open?profile=openclaw', 'POST', b'{"url":"https://www.google.com"}'),
    ('tabs?profile=openclaw', 'GET', None),
    ('snapshot?profile=openclaw', 'GET', None),
]
for path, method, body in checks:
    req = urllib.request.Request(base + path, method=method, data=body, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            print(f'\nPATH {path} STATUS {r.status}')
            print(r.read(5000).decode('utf-8', 'ignore'))
    except urllib.error.HTTPError as e:
        print(f'\nPATH {path} HTTP {e.code}')
        print(e.read(5000).decode('utf-8', 'ignore'))
    except Exception as e:
        print(f'\nPATH {path} ERR {e!r}')

for url in [r'http://127.0.0.1:18800/json/version', r'http://127.0.0.1:18800/json/list']:
    try:
        with urllib.request.urlopen(url, timeout=3) as r:
            print(f'\nCDP {url} STATUS {r.status}')
            print(r.read(1000).decode('utf-8', 'ignore'))
    except Exception as e:
        print(f'\nCDP {url} ERR {e!r}')
