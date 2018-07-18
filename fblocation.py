import re

with open('../Desktop/facebook-mindau/location_history/your_location_history.html','r') as fl:
    for line in fl:
        geo=re.findall(r'[+-]?\d+\.\d+,\s[+-]?\d+\.\d+',line)

with open('../Desktop/file.txt','w') as coord:
    for i in range(len(geo)):
        lat, long = geo[i].split(sep=', ')
        coord.write(lat+' '+long+'\n')
