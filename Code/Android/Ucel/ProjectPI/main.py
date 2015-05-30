__author__ = 'Johannes'
from test.Bruch import Bruch
from random import randint
if __name__ == '__main__':
    b1=Bruch(3,4)
    b2=Bruch(3,4)+b1
    z1,z3=b1
    b3=3+b1+Bruch(1,4)
    b4=3/b3+3
    b3+=Bruch(3,2)
    b0=Bruch(4,3)
    print(str(b1)+" == invert "+str(b0),b1== ~b0 )
    print(b3)
    b3=-b3
    print(b3 is not b2)
    b5=Bruch(b3.zaehler,b3.nenner)
    print(b3 is b5)
    b4=4*b4-Bruch(2,4)-b3**2
    print(b1,'=',float(b1))
    print(hex(int(b1+123)))
    print(oct(int(b1+123)))
    print(int(b1+123))
    print(b2,'=',float(b2))
    print(b3,'=',float(b3))
    print(b4,'=',float(b4))
    print("abs%s ="%(b4),abs(b4))
