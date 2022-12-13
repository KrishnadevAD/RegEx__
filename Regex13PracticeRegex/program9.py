# 7) Write a Python program to find sequences of lowercase letters joined with a underscore.( starting with underscore)
import re
text='''
krishnadev Adhikari ac aacc abb abbb accc  _abb,_ab_bb,abbbb,abb_bbb, _abbbbbb abbbbb hikjkkk
'''
pattern =re.compile(r'_?[a-z]+_[a-z]+')
match =re.finditer(pattern,text)

for m in match:
    print(m)