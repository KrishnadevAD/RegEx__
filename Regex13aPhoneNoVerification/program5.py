import re
import os
file = os.path.join(os.getcwd(),r"C:\Users\DELL\Desktop\data science DWIT\day13\RegexSample.txt")
fileopen = open(file,"r")
fileData = fileopen.read()

emergencyNumbers = []
panNumber = []
phoneNumber = []
emergencyNumberPattern = re.compile(r'10[0124]\n')
panNumberPattern = re.compile(r'[613]\d{8}\n')
#Compile a regular expression pattern, returning a Pattern object.
# phonePattern = re.compile(r'(98)\d\d\d\d\d\d\d\d\n')

matchesEmergency = re.findall(emergencyNumberPattern,fileData)
matchesPan = re.findall(panNumberPattern,fileData)
# matchesPhone = re.findall(phonePattern,fileData)

for match in matchesEmergency:
    emergencyNumbers.append(match[:-1])

for match in matchesPan:
    panNumber.append(match[:-1])

# for match in matchesPhone:
#     phonePattern.append(match[:-1])

print("Th emergency Numbers are : ",emergencyNumbers)
print("The Pan Numbers are :",panNumber)
# print("The Phone Numbers are:",phonePattern)