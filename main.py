def Determinant(a,b,c):
    D = (b**2-4*a*c)**0.5
    return D
def sol1(a,b,c):
    s1 = (-b+Determinant(a,b,c))/(2*a)
    return s1
def sol2(a,b,c):
     s2 = (-b-Determinant(a,b,c))/(2*a)
     return s2
Eqn = input("Enter your equation(ax^2+bx+c): ")
x1 = sol1(int(Eqn[0]),int(Eqn[5]),int(Eqn[8]))
x2 = sol2(int(Eqn[0]),int(Eqn[5]),int(Eqn[8]))
print("The solutions are %d and %d" %(x1,x2))
