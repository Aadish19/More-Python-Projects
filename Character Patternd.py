n=int(input())
i=1
while i<=n:
    j=1
    start_char=chr(ord('A')+j-1)
    while j<=i:
        
        print(start_char,end="")
        j+=1
    print()
    i+=1

