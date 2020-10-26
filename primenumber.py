class PrimeNumber:

    def prime_number(self):
        num = int(input("Enter the number: "))

        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    print(num, " is not a prime number")
                    print(i, "times" ,num//i, "is" ,num)
                    break

            else:
                print(num, " is prime number")

        else:
            print(num, "is not prime number")


    def prime_number_list(self):

        lower = int(input("Enter the lower number: "))
        upper = int(input("Enter the upper number: "))

        for num in range(lower, upper + 1):
            if num > 1:
                for i in range(2, num):
                    if (num % i) == 0:
                        break

                else:
                    print(num)





pm = PrimeNumber()
pm.prime_number_list()