# 6) Write a Python program that matches a string that has an a followed by two to three 'b'.
# working as a range 
#ab{2,6}'-- -> abb,abbb,abbbb,abbbbb, abbbbbb   bhako print garxa yesle
import re
text='''
krishnadev Adhikari ac aacc abb abbb accc  abb,abbb,abbbb,abbbbb, abbbbbb abbbbb hikjkkk
'''
pattern =re.compile(r'ab{2,6}')
match =re.finditer(pattern,text)

for m in match:
    print(m)