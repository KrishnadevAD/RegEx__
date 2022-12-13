import re
text_to_search = '''
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

logisparktech.com

321-555-4321
123.444.1234
456*697*5566
800-123-234
900-234-123


192.168.1.91

Mr Rohit
Mr. Raunak
Ms. Anushka
Mrs. Nisha
Mr. T


cat
mat
pat
bat
'''
mt_scentence='start a scentence and bring it to  and end '
# raw string
print(r"Krishnadev adhikari \t Danuwar ")

# pattern 
#Compile a regular expression pattern, returning a Pattern object.
pattern = re.compile(r'Mr\.?\s[A-Z]')
# MATCHING  a regex , finditer  returns and iterable

matches = re.finditer(pattern,text_to_search)

for match in matches:
    print(match)