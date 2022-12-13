import re
url = '''
https://www.google.com
http://logidhdjjdjdjsparltech.com
https://logiskkkkhdparktech.com
https://wwww.iodjdjdjost.gov
'''

#grouping the Urls
pattern = re.compile(r'https?://(www.)?(\w+)(\.\w+)')

matches = pattern.finditer(url)
#creating a patter of sub url( substitution group 3 and group 3)
#getting only top leve domain
subbed_urls = pattern.sub(r'\2\3',url)
print(subbed_urls)

for match in matches:
    # print(match)

#match method has the index of object that we want to see
    print(match.groups())
    #match .group(index) give the index of the group that we want
    print(match.group(1))