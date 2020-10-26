

def fact_recur(n):
    if n == 1:
        return n
    else:
        return n*fact_recur(n-1)


num = int(input("Enter the number : "))

if num < 0:
    print("Factorial number is not present for - ve numbers")

elif num == 0:
    print("Factorial of 0 is 1")

else:
    print("print the factorial of", num, "is", fact_recur(num))

