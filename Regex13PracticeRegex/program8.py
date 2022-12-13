# 7) Write a Python program to find sequences of lowercase letters joined with a underscore.
import re
text='''
krishnadev Adhikari ac aacc abb abbb accc  abb,ab_bb,abbbb,abb_bbb, abbbbbb abbbbb hikjkkk
'''
pattern =re.compile(r'[a-z]+_[a-z]')
match =re.finditer(pattern,text)

for m in match:
    print(m)