 # regex url 
import re

url ='''
https://www.google.com
http://logidhdjjdjdjsparltech.com
https://logiskkkkhdparktech.com
https://wwww.iodjdjdjost.gov

''' 
pattern = re.compile(r'https?://(www.)?')
##matches=re.finditer(pattern,url)

matches = pattern.finditer(url)
#creating a patter of sub url( substitution group 3 and group 3)
#getting only top leve domain
#subbed_urls = pattern.sub(r'\2\3',url)
#print(subbed_urls)

for match in matches:
    print(match)