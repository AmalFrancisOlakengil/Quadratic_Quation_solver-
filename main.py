def Determinant(a,b,c):
    D = float((b**2-4*a*c)**0.5)
    return D
def sol1(a,b,c):
    s1 = (-b+Determinant(a,b,c))/(2*a)
    return s1
def sol2(a,b,c):
     s2 = (-b-Determinant(a,b,c))/(2*a)
     return s2
print("For equation ax^2+bx+c")
values = input("Enter the a,b and c values:")
Eqn = values.split()
x1 = sol1(int(Eqn[0]),int(Eqn[1]),int(Eqn[2]))
x2 = sol2(int(Eqn[0]),int(Eqn[1]),int(Eqn[2]))
print("The solutions are %f and %f" %(x1,x2))
