# 3) Write a Python program that matches a string that has an a followed by one or more c's
import re
text_to_search = '''
Microsoft and our third-party vendors use cookies to store and access information
 such as unique IDs to deliver, maintain and improve our services and ads. If you agree,
  MSN and Microsoft Bing will personalise the content and ads that you see. 
  You can select ‘I Accept’ to consent to these uses or click on ‘Manage preferences’ to
 review your options and exercise your right to object to Legitimate Interest where used. 
 2333334444
 4444444984y4i40
 WWWWW


'''
#mt_scentence='start a scentence and bring it to  and end '
# raw string
#print(r"Krishnadev adhikari \t Danuwar ")

# pattern 
#Compile a regular expression pattern, returning a Pattern object.
pattern = re.compile(r'a[c+]')
# MATCHING  a regex , finditer  returns and iterable

matches = re.finditer(pattern,text_to_search)

for  match  in  matches:
    print("True ")
    break;
print('false')
    
    