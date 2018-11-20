#first part
def everyother(s):
    ret = ""
    i = True
    for char in s:
        if i:
            ret += char.upper()
        else:
            ret += char.lower()
        if char != ' ':
            i = not i
    return ret
new_line = everyother(raw_input('Enter a phrase: '))
print new_line

#second part
newer_line = new_line.replace('A', '*')
brand_line = newer_line.replace('E', '*')
brander_line = brand_line.replace('I', '*')
brandest_line = brander_line.replace('O', '*')
final_line = brandest_line.replace('U', '*')
print final_line

#third part
open_par = final_line.count('(')
close_par = final_line.count(')')
if open_par == close_par:
    print "Balanced? True"
else:
    print "Balanced? False"
