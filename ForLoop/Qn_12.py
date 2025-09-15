#count letters, digtis and special alphabets from the given string:

a = 'nclkncnc@!!&*1234'

char= 0
digits = 0
schar =0

for i in a:
    if i.isdigit():
        digits+=1
    elif i.isalpha():
        char+=1
    else:
        schar+=1

print(f"char = {char}\n digits = {digits}\n schar = {schar}")