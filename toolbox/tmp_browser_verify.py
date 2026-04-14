import json
import urllib.request
import urllib.error

cfg = json.load(open(r'C:\Users\marco\.openclaw\openclaw.json', 'r', encoding='utf-8'))
token = cfg['gateway']['auth']['token']
base = 'http://127.0.0.1:18791/'
headers = {'Authorization': 'Bearer ' + token, 'Content-Type': 'application/json'}

def go(path, method='GET', body=None):
    req = urllib.request.Request(base + path, data=body, method=method, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=25) as r:
            print(f'\nPATH {path} STATUS {r.status}')
            print(r.read(4000).decode('utf-8', 'ignore'))
    except urllib.error.HTTPError as e:
        print(f'\nPATH {path} HTTP {e.code}')
        print(e.read(4000).decode('utf-8', 'ignore'))
    except Exception as e:
        print(f'\nPATH {path} ERR {e!r}')

go('?profile=openclaw')
go('tabs?profile=openclaw')
go('tabs/open?profile=openclaw', 'POST', b'{"url":"https://www.google.com"}')
go('tabs?profile=openclaw')
go('snapshot?profile=openclaw')
