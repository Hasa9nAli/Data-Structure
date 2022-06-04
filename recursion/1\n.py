# 1/1 + 1/2 + 1/3 + 1/4 +... 1/n 
def sum(n):
    if n == 1:
        return 1 
    else : 
        return (1/n) + sum(n-1)

print(sum(5))
