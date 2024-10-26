# Python3 program to find simple interest
#  principal amount, time and
# rate of interest taken from user.


def simple_interest(pt,tm,rt):
    print('The principal is', pt)
    print('The time period is', tm)
    print('The rate of interest is',rt)
    
    si = (pt * tm * rt)/100
    
    print('The Simple Interest is', si)
    
    
# Driver code
P = int(input("Enter the principal amount :"))
T = int(input("Enter the time period :"))
R = int(input("Enter the rate of interest :"))
simple_interest(P,T,R)
