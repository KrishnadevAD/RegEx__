# use of regex is : password , phone no , email cheching ko lagi  use garxa 
import re
text=" Hello My Name is KrishnaDev"
regex_to_match = 'Hello'

##  uses:
# search--> euta match bhako object returns gardinxa 
result = re.search(regex_to_match,text)
print("search",result)
print("#########################")
# string
print("Returning String",result.string)
print("#########################")
# span
print("Returning Span",result.span())
print("#########################")
# group
print("Returning group",result.group())
print("#########################")


result2 = re.findall(regex_to_match,text)
print("find all",result2)
print("#########################")

result3 = re.split(regex_to_match,text)
print("split",result3)

#  malaai chai ke chahiyou bhane  starting with " hello " suruko matra chahiyou 
text2="hello my name is KrishnaDev adhikari pp"
print("Starting with ",re.search('hello',text2))
# stating with hello 
text2="hello my name is KrishnaDev adhikari pp"
print("Starting with ",re.search('^hello',text2).span())

# Ending with hello 
text2="hello my name is KrishnaDev adhikari pp"
print("Starting with ",re.search('hello$',text2).span())