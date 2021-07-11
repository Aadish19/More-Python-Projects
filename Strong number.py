
n=int(input())
suma=0
fact=1
t=n
while t>0:
    digit=t%10
    suma=suma+(fact*digit)
    t=t//10

if n==t:
    print("Strong")
else:
    print("Not Strong")

    
