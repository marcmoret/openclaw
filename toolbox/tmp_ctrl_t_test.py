import json, urllib.request, time
cfg = json.load(open(r'C:\Users\marco\.openclaw\openclaw.json', 'r', encoding='utf-8'))
headers = {'Authorization': 'Bearer ' + cfg['gateway']['auth']['token'], 'Content-Type': 'application/json'}
base = 'http://127.0.0.1:18791/'

def req(path, method='GET', body=None):
    request = urllib.request.Request(base + path, method=method, data=body, headers=headers)
    with urllib.request.urlopen(request, timeout=30) as r:
        return r.read().decode('utf-8', 'ignore')

print('STATUS_BEFORE')
print(req('?profile=openclaw'))
print('TABS_BEFORE')
print(req('tabs?profile=openclaw'))
print('OPEN_GOOGLE')
print(req('tabs/open?profile=openclaw', 'POST', b'{"url":"https://www.google.com"}'))
time.sleep(2)
print('TABS_AFTER_OPEN')
print(req('tabs?profile=openclaw'))
