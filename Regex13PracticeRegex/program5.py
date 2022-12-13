# 5) Write a Python program that matches a string that has an a followed by three 'b'
import re
text='''
krishnadev Adhikari ac aacc abbb accc hikjkkk
'''
pattern =re.compile(r'ab{3}')
match =re.finditer(pattern,text)

for m in match:
    print(m)