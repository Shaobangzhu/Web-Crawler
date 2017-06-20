import requests

url = "https://item.jd.com/1698961234.html?jd_pop=fa11cbec-58fd-44b9-8597-89da31033aee&abt=0"
try:
    r = requests.get(url)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[:1000])
except:
    print("failure")