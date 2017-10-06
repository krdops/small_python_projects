
import re


string = "new table (table1) ["
pat = re.compile(r'([^(]+)\s*\(([^)]+)\)\s*(?:\s*|$)')

lst = [(t[1].strip()) for t in pat.findall(string)]

print(lst)


