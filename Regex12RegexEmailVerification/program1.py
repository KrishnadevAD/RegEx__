# email verification
import re
emails='''
 PrdhfhhfhfayukjjjjhSkkrestha@gmail.com
 phfhfhhfrayujjjjsh.shrestjkknnha@logisparktech.org
 prfhfayhfjfhfush-321-shrejjjjstha@deerwalk.edu.np
 pfhfjfrayjfjjfkkfkkush123@my-work.net
'''
pattern = re.compile(r'\w+@\w+\.com')

matches = re.finditer(pattern,emails)

for match in matches:
    print(match)

