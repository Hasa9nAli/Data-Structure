# power number using recursion

def power(number, n ) : 
    if n == 0: 
        return 1
    else: 
        return number * (power(number, n-1))
    # 2 * 2 * 2
print(power(2,3))
