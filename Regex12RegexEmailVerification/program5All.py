import re
emails = '''
KrishnDevAdhikari@gmail.com
krishnadev.adhikri@kridara.org
krishnadev-321-adhikarai@kridara.edu.np
kridara123@my-work.net

'''

# #matching first email
pattern = re.compile(r'[a-zA-Z]*@[a-zA-z]+\.com')
# #Matching second email
pattern = re.compile(r'[a-zA-Z.]*@[a-zA-z]+\.(com|org)')

#Matching third email
pattern = re.compile(r'[a-zA-Z0-9.-]*@[a-zA-z]+\.(com|org|edu)(\.np)?')

#Matching third email
pattern = re.compile(r'[a-zA-Z0-9.-]*@[a-zA-z-]+\.(com|org|edu|net)(\.np)?')

sampleemailre = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
matches = pattern.finditer(emails)
for match in matches:
    print(match)