
def recur_natural(n):

    if n <= 1:
        return n
    else:
        return n + recur_natural(n-1)

num = int(input("How many terms? : "))

if num < 0:
    print("Enter a positive number")

else:
    print("The sum is ", recur_natural(num))