E = 26.5
r1 = 31.4
r2 = 0.8
r3 = 0.8 
r4 = 6.4
r5 = 7.1 
r6 = 7.1 
r7 = 7.1 
r8 = 7.1 

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
    r85y, r48y, r45y = delta_star(r8, r5, r4)
    r7__ = r7 + r48y
    r6__ = r6 + r45y
    r6_7 = parallel(r7__, r6__)
    r2__ = r85y + r6_7 + r2 + r3
    r_eq = parallel(r1, r2__)
    I = E / r_eq
    P = I * E
    p_r1 = (E ** 2) / r1
    print("R equivalent: ", r_eq)
    print("Current: ", I)
    print("Power: ", P)
    print("Power_R1: ", p_r1)

main()