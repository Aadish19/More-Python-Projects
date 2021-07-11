a=12345678
i=0
while a!=0:
    rem=a%10
    print(rem)
    a=a//10
    if rem%2!=0:
        i=i+1
    print("i is {}".format(i))
