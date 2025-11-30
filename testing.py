a = "string"
b = "jatoch"
import re
string = "ha: (kapot, nee, ja, oke stop.)\n jatog"
inhoud = re.search(r'\((.*?)\)', string)
match = inhoud.group(1)
print(match)