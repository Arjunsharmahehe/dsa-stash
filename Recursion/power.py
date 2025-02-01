def power(x: int, n: int) -> int:
    if n == 0:
        return 1
    
    return x*power(x, n-1)


print(power(5, 25))