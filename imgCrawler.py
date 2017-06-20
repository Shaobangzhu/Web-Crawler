import requests
import os

url = "http://images.ali213.net/picfile/pic/2015/06/15/927_2015061595240120.jpg"
root = "/Users/chaoranlu/Documents/tmpImg/"
path = root + url.split('/')[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close()
            print("file saved successfully")
    else:
        print("file already exists")
except:
    print("Failure")
