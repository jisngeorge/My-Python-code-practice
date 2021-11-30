p = input()
q = input()
output = str()
if len(p) == len(q):
    output = "true"
else:
    output = "false"
#print(output)
output += " " + str(ord(q[len(q) - 1]))
#print(output)
vowels = 0
for i in p + q:
    if i in 'aeiou':
        vowels += 1
output += " " + str(vowels)
print(output)
