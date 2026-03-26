E = 31.4
r1 = 23.9
r2 = 12.4
r3 = 12.4 
r4 = 12.4
r5 = 6.2 
r6 = 6.2 
r7 = 6.2 
r8 = 6.2 

def parallel(a, b):
    return  (a*b)/(a+b)



def star_delta(r1,r2,r3):   # example, if I want to get resistor r1_2
    ra =  r1+r2+(r1*r2)/r3  # you have to put first and second argument r1 and r2 
    rb =  r2+r3+(r2*r3)/r1  # order of r1 and r2 doesnt matter(it can be r2 and r1)
    rc =  r1+r3+(r1*r3)/r2
    return ra,rb,rc

def delta_star(ra,rb,rc): #same logic here
    sum =  ra+rb+rc
    r1 =  (ra*rb)/sum
    r2 =  (rb*rc)/sum
    r3 =  (ra*rc)/sum
    return r1, r2, r3

def a():
    r6_7 = r6+r7
    r5_8 = r5+r8
    r24del, r467del, r267del = star_delta(r4, r2, r6_7)
    r58_24 = parallel(r5_8, r24del)
    r3_467 = parallel(r3, r467del)
    r24__ = r58_24 + r3_467
    r267__ = parallel(r24__, r267del)
    r_eq = parallel(r267__, r1)
    I = E / r_eq
    P = I * E
    print("R_a equivalent: ", r_eq)
    print("Current_a: ", I)
    print("Power_a: ", P)
a()

print("-------------------------------")

def b():
    r27y, r57y, r25y =  delta_star(r2, r7, r5)
    r68y, r38y, r36y = delta_star(r6, r8, r3)
    r4__ = r27y + r4 + r38y
    r68_57 = r68y + r57y
    r68__ = parallel(r4__, r68_57)
    r25__ = r25y + r68__ + r36y
    r_eq = parallel(r1, r25__)
    I = E / r_eq
    P = I * E
    print("R_b equivalent: ", r_eq)
    print("Current_b: ", I)
    print("Power_b: ", P)
b()