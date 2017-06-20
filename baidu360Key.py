import requests

keyword = "Python"
try:
    kv = {'q': keyword}
    r = requests.get("http://www.so.com/s", params=kv)
    print(r.request.url)
    r.raise_for_status()
    print(len(r.text))
except:
    print("Failure")