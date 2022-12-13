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

scentense = 'Start a scentense and bring it to and end'


def phoneFilter(fnPattern):
    with open(r'C:\Users\DELL\Desktop\data science DWIT\day12\phone.txt', 'r') as f:
        contents = f.read()

        matches = fnPattern.finditer(contents)

        for match in matches:
            print(match)


#rawstring is a string to ignore blackslash
# print("\tn")
# print(f"\tn")

#using compile to compilre regex before using , compile gives power to add multiple regex

#this returns matched abc only , is case sensitive
pattern = re.compile(r'abc')

#this returns matched abc only , is case sensitive
pattern = re.compile(r'ABC')

#escape character \ can be used | . is used to denote all except newline character
pattern = re.compile(r'.')

#To escape the use of . we can use \ returns all the .
pattern = re.compile(r'\.')

#example matching url
pattern = re.compile(r'logisparktech\.com')

#exmple of word boundry
pattern = re.compile(r'\bHa')

#matching ha without word boundry
pattern = re.compile(r'\BHa')

#start and end
pattern = re.compile(r'^Start')
pattern = re.compile(r'^a')
pattern = re.compile(r'end$')
pattern = re.compile(r'a$')
matches = pattern.finditer(scentense)

#matching phone number
#basic pattern
#matches all phone number
#this pattern matches any character in between phone number which can cause error
pattern = re.compile('\d\d\d.\d\d\d.\d\d\d\d')
phoneFilter(pattern)

#to fix use character set matches only one character and we do not have to include back slash
#try with double dash
pattern = re.compile('\d\d\d[.-]\d\d\d[.-]\d\d\d')

#matching 800 or 900 numbers
pattern = re.compile(r'[89]00[.-]\d\d\d[.-]\d\d\d')
#matches 800 and 900 starting number only
phoneFilter(pattern)

#using dash with bract gives a set [a-z] matches digit from a -z
#matches all characters from a-z and A-Z to add simply add after it
pattern = re.compile(r'[a-zA-z]')

#using caret here negates the character set i.e matches everything not in the set
pattern = re.compile(r'[^a-zA-z]')


#match all the character ending with at except for b
pattern = re.compile(r'[^b]at')

#mathing phone number again
pattern = re.compile(r'\d{3}.\d{3}.\d{4}')

#Matching Mr not matching the one without .
pattern = re.compile(r'Mr\.')

#mathinc with . ? = or or one
pattern = re.compile(r'Mr\.?')

#matching with name with Mr. and first letter
pattern = re.compile(r'Mr\.?\s[A-Z]')

#matching with name with Mr. and full name \w matches word * matches 0 or more
pattern = re.compile(r'Mr\.?\s[A-Z]\w*')

#matching mrs. and all
pattern = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*')

matches = pattern.finditer(text_to_search)
#MATHCES NOW HAS AN ITERABLE THAT WE CAN ITERATE ON
for match in matches:
    print(match)
