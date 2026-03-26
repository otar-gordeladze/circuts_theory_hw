r1 = 84.1
r2 = 13
r3 = 10.4
r4 = 46.5
r5 = 6.7
r6 = 26.7
r7 = 12
r8 = 12
r9 = 30.9
r10 = 30.9
r11 = 18.1
r12 = 18.1


def parallel(a, b):
    return  (a*b)/(a+b)



def star_delta(r1,r2,r3):
    ra =  r1+r2+(r1*r2)/r3
    rb =  r2+r3+(r2*r3)/r1
    rc =  r1+r3+(r1*r3)/r2
    return ra,rb,rc

def delta_star(ra,rb,rc): #same logic here
    sum =  ra+rb+rc
    r1 =  (ra*rb)/sum
    r2 =  (rb*rc)/sum
    r3 =  (ra*rc)/sum
    return r1, r2, r3

def ab():
    r12del, r13del, r23del = star_delta(r2, r1, r3)
    r911y, r711y, r79y = delta_star(r9, r11, r7)
    r812y, r1012y, r810y = delta_star(r8, r12, r10)
    
    r13_4 = parallel(r13del, r4)
    r23_5 = parallel(r23del, r5)
    r13_4_23_5 =  r13_4 + r23_5
    r12_13__ = parallel(r12del, r13_4_23_5)
    r6_12__ = parallel(r6, r12_13__)
    r79_6_810 =  r79y + r6_12__ + r810y
    r711y_812y =  r711y + r812y
    r711__ = parallel(r79_6_810, r711y_812y)
    r_eq =  r911y + r711__ + r1012y
    print(r_eq)

ab()

def cd():
    r11_9 = r11+r9
    r12_10 = r12 + r10
    r8__ = parallel(r12_10, r8)
    r7__ = parallel(r11_9, r7)
    r7_8 = r8__ + r7__
    r6__ = parallel(r7_8, r6)
    r12del, r13del, r23del = star_delta(r2, r1, r3)
    r12__ = parallel(r6__, r12del)
    r23__ = parallel(r5, r23del)
    r12_23 = r12__ + r23__
    r13__ = parallel(r12_23, r13del)
    r_eq = parallel(r13__, r4)
    print(r_eq)

cd()


