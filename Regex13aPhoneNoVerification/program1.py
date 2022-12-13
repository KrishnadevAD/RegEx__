import re
text_to_search = '''
9843065157
+977-9841511769
1234567
552245
01-5553731
+977-015553732
9801224453
9841779580
5919540
009779841980446
124457894
102
9818000061
9808445280
98187460212
100
+85255154280
+61426002960
911
103
+1989770-3121
+32488194676
+91986432451
+86159014875
+917892348916
7892348916
911
119
021-577387
5154579
513341
513344
606651925
AAACB1534F
AAACB0472C
610279391
135067299
303625409
500199240






'''
#mt_scentence='start a scentence and bring it to  and end '
# raw string
#print(r"Krishnadev adhikari \t Danuwar ")

# pattern 
#Compile a regular expression pattern, returning a Pattern object.
pattern = re.compile(r'(98)\d\d\d\d\d\d\d\d')
# MATCHING  a regex , finditer  returns and iterable

matches = re.finditer(pattern,text_to_search)

for match in matches:
    print(" The  mobile number \n ",match)