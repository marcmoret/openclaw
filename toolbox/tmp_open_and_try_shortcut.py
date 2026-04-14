import json, urllib.request, time
cfg = json.load(open(r'C:\Users\marco\.openclaw\openclaw.json', 'r', encoding='utf-8'))
headers = {'Authorization': 'Bearer ' + cfg['gateway']['auth']['token'], 'Content-Type': 'application/json'}
base = 'http://127.0.0.1:18791/'
url = 'https://x.com/akshay_pachaar/status/2044000393110474756?s=46'
req = urllib.request.Request(base + 'tabs/open?profile=openclaw', method='POST', data=json.dumps({'url': url}).encode('utf-8'), headers=headers)
with urllib.request.urlopen(req, timeout=30) as r:
    print(r.read().decode('utf-8', 'ignore'))
time.sleep(2)
req = urllib.request.Request(base + 'snapshot?profile=openclaw', headers={'Authorization': 'Bearer ' + cfg['gateway']['auth']['token']})
with urllib.request.urlopen(req, timeout=30) as r:
    print(r.read(4000).decode('utf-8', 'ignore'))
