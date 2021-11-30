'''
        Molecule Question
'''
c, h, o = map(int,input("Enter the atoms: ").split(" "))

g = (4*c - 2*o + h)/24
w = (2*o - 4*c + h)/4
x = (2*o - h)/4 

if(g<0 or w<0 or x<0):
    print("error")
elif(int(g)!=g or int(w)!=w or int(x)!=x):
    print("error")
else:
    print(int(w)," ",int(c)," ",int(g))
