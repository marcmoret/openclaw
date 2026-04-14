import json
import urllib.request
import urllib.error

url = 'https://x.com/neoaiforecast/status/2043455838459920718?s=46'
cfg = json.load(open(r'C:\Users\marco\.openclaw\openclaw.json', 'r', encoding='utf-8'))
token = cfg['gateway']['auth']['token']
base = 'http://127.0.0.1:18791/'
headers = {'Authorization': 'Bearer ' + token, 'Content-Type': 'application/json'}

def go(path, method='GET', body=None):
    req = urllib.request.Request(base + path, data=body, method=method, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            print(f'\nPATH {path} STATUS {r.status}')
            print(r.read(5000).decode('utf-8', 'ignore'))
    except urllib.error.HTTPError as e:
        print(f'\nPATH {path} HTTP {e.code}')
        print(e.read(5000).decode('utf-8', 'ignore'))
    except Exception as e:
        print(f'\nPATH {path} ERR {e!r}')

go('?profile=openclaw')
go('tabs/open?profile=openclaw', 'POST', ('{"url":' + json.dumps(url) + '}').encode('utf-8'))
go('tabs?profile=openclaw')
go('snapshot?profile=openclaw')
