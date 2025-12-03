a = "string"
b = "jatoch"
import re
string = "ha: (kapot, nee, ja, oke stop.)\n jatog"
char1 = string.find("(")
char2 = string.find(")")
check = string[char1+1 : char2]
print(check)