# 6) Write a Python program that matches a string that has an a followed by two to three 'b'.
import re
text='''
krishnadev Adhikari ac aacc abb abbb accc abbbbb hikjkkk
'''
pattern =re.compile(r'ab{2,3}')
match =re.finditer(pattern,text)

for m in match:
    print(m)