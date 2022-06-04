# recursion factorial number  
def fact(n):
    if n == 0: return 1 
    else: return(n*fact(n-1))
    # 5 * 4 * 3 * 2 * 1 => 120 

print(fact(5))
