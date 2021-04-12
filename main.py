n = int(input())
big = -n
prebig2 = -n
for i in range(n):
    a = int(input())
    if a > big:
        prebig2 = big
        big = a
    else:
        if a < big and a > prebig2:
            prebig2 = a
print(big, prebig2, sep='\n')