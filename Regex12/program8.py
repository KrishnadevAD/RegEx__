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
800-123-2343
900-234-1235


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
#   [.-] for both
#[89]00 first ma 9 ki na bhaye 8 herxa  ani  tyespaxi chai tyesle chai - check garxa hai 
pattern = re.compile(r'[89]00[-]\d\d\d[-]\d\d\d\d')
# MATCHING  a regex , finditer  returns and iterable

matches = re.finditer(pattern,text_to_search)

for match in matches:
    print(match)