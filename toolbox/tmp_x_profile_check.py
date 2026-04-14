import json, urllib.request, urllib.error
cfg = json.load(open(r'C:\Users\marco\.openclaw\openclaw.json', 'r', encoding='utf-8'))
headers = {'Authorization': 'Bearer ' + cfg['gateway']['auth']['token'], 'Content-Type': 'application/json'}
base = 'http://127.0.0.1:18791/'
ops = [
    ('tabs/open?profile=openclaw', 'POST', b'{"url":"https://x.com/neoaiforecast/status/2043455838459920718?s=46"}'),
    ('tabs?profile=openclaw', 'GET', None),
    ('snapshot?profile=openclaw', 'GET', None),
]
for path, method, body in ops:
    req = urllib.request.Request(base + path, method=method, data=body, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            print(f'PATH {path} STATUS {r.status}')
            print(r.read(12000).decode('utf-8', 'ignore'))
            print()
    except urllib.error.HTTPError as e:
        print(f'PATH {path} HTTP {e.code}')
        print(e.read(12000).decode('utf-8', 'ignore'))
        print()
    except Exception as e:
        print(f'PATH {path} ERR {e!r}')
        print()
