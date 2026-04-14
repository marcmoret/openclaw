import json, urllib.request, urllib.error, time
cfg = json.load(open(r'C:\Users\marco\.openclaw\openclaw.json', 'r', encoding='utf-8'))
headers = {'Authorization': 'Bearer ' + cfg['gateway']['auth']['token'], 'Content-Type': 'application/json'}
base = 'http://127.0.0.1:18791/'

def call(path, method='GET', body=None, timeout=30):
    req = urllib.request.Request(base + path, method=method, data=body, headers=headers)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.status, r.read().decode('utf-8', 'ignore')

post_url = 'https://x.com/akshay_pachaar/status/2044000393110474756?s=46'
popup_url = 'chrome-extension://cnjifjpddelmedmihgijeibhnjfabmlf/popup.html'

for url in [post_url, popup_url]:
    status, body = call('tabs/open?profile=openclaw', 'POST', ('{"url":"' + url + '"}').encode('utf-8'))
    print('OPEN', url, status)
    print(body[:4000])
    print()
    time.sleep(1)

status, body = call('tabs?profile=openclaw')
print('TABS', status)
print(body[:12000])
print()

time.sleep(1.5)
status, body = call('snapshot?profile=openclaw')
print('SNAPSHOT', status)
print(body[:12000])
