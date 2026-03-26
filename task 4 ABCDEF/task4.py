r1 = 8.7
r2 = 3.5
r3 = 17.8 
r4 = 6.6
r5 = 25.8
r6 = 4.3
r7 = 42.4 
r8 = 11.7
r9 = 6.4
r10 = 7.1 
r11 = 13.3 
r12 = 31.6
r13 = 8.7 
r14 = 27.4 
r15 = 5.9 
r16 = 0.7 

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


def ab():
    r5__ = parallel(r5, r6)
    r4__ = r4 + r5__
    r3__ = parallel(r4__, r3)
    r2__ = r3__ + r2
    r_eq = parallel(r2__, r1)
    print("AB-R equivalent: ", r_eq)

def cd():
    r13__ = parallel(r13, r14)
    r_eq = r15 + r13__ + r16
    print("CD-R equivalent: ", r_eq)

def ef():
    r11__ = parallel(r11, r10)
    r12__ = parallel(r11__, r12)
    r8__ = r8 + r12__ + r9
    r_eq = parallel(r8__, r7)
    print("EF-R equivalent: ", r_eq)

ab()
cd()
ef()