import re
s = "https:1.qdhffhttps:2.qfjhfhhttps:3.qfhjfhshttps:4.qdfdg"
l = re.findall(r'https.*?.',s)
print(l)