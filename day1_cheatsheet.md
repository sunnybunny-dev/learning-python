##Day1 Cheat Sheet

##1.String Essentials
 **Raw Strings ('r""'):** Ignore escape characters (e.g., '\n','\t').Perfect for regex and window paths.

path = r"C:\new_folder\file.txt"

F-Strings(f""):Best way to inject variables into text.

2.Basic Regex (import re)

re.findall (pattern, text)
#It searches the entire text, collects every single match it finds, and gives them all back to you in a standard list of text strings.

re.search(pattern,text)
#It scans until it finds the very first match
e.g:
import re
text = "I have 2 cats and 3 dogs"
#findall grabs all numbers as a simple list:
print(re.findall(r"\d"), text)
#output:['2' ,'3']

#search grabs only the first number inside a match box
match = re.search (r"\d", text)
print(match.group())
# output: 2


