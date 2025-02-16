def fibonacci(n):
    if n <= 1:
        return n
    else:
        return(fibonacci(n-1) + fibonacci(n-2))
n = int(input("Enter the number of terms: "))
for i in range(n):
    print(fibonacci(i))

## Or



# def fibonacci(n, memo={}):
#     if n in memo:
#         return memo[n]
#     if n <= 1:
#         return n
#     memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
#     return memo[n]

# n = int(input("Enter the number of terms: "))
# for i in range(n):
#     print(fibonacci(i))
