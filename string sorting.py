# You are given a string .
#  contains alphanumeric characters only.
#  Your task is to sort the string  in the following manner:
#
# All sorted lowercase letters are ahead of uppercase letters.
# All sorted uppercase letters are ahead of digits.
# All sorted odd digits are ahead of sorted even digits.


mystr = input()

mylst = []

for x in mystr:
    mylst.append(x)

print(mylst)
mylst.sort()
upperstr = ''
lowerstr = ''
nume = ''
evennume=''
oddnume=''
for x in mylst:
    if x.isnumeric():
        nume+=x
    if x.isupper():
        upperstr+=x
    if x.islower():
        lowerstr+=x
print(mylst)
for y in nume:
    y=int(y)
    if y%2!=0:
        y=str(y)
        oddnume+=y
    else:
        y=str(y)
        evennume+=y
print(lowerstr+upperstr+oddnume+evennume)

# Sorting1234
#  o/p - ginortS1324