import re

geo = [['latitude','longitude']]

with open('../Desktop/Dropbox/loc.txt','r') as fl:
    for line in fl:
        geo.append(re.findall(r'[+-]?\d+\.\d+',line))

print(geo)
