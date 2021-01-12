import requests
import hashlib
import re

req = requests.session()
url1 = "http://159.65.88.44:31883/"

# -- get request --
rget = req.get(url1)
html = rget.content.decode('utf-8') # convert html (a byte-like object) into a string
# print (html)

# -- strip html --
def html_tags(html):
    clean = re.compile('<.*?>')
    return re.sub(clean, '', html)
# print (html_tags(html))

# -- split string -- 
out1 = html_tags(html)
out2 = out1.split('string')[1]
# print (out2)
out3 = out2.rstrip()
print (out3)
out4 = out3.encode('utf-8')
# print (out4)

# -- MD5 encryption --
mdHash = hashlib.md5(out4).hexdigest()
print (mdHash)

# -- post request --
data1 = dict(hash=mdHash)
rpost = req.post(url=url1, data=data1)
print (rpost.text)
