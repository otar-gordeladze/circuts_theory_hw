E = 7.6
r1 = 2.1
r2 = 8.7
r3 = 1.1 
r4 = 7.1
r5 = 3.6

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


def main():
    r4__ = parallel(r5,r4)
    r3__ = r4__ + r3
    r2__ = parallel(r3__, r2)
    r_eq = r2__ + r1
    I = E / r_eq
    P = I * E
    p_r1 = (I ** 2) * r1
    print("R equivalent: ", r_eq)
    print("Current: ", I)
    print("Power: ", P)
    print("Power R1: ", p_r1)

main()