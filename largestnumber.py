class LargestNumber:

    def largest_number(self):
        a = float(input('Enter first number: '))
        b = float(input('Enter second number: '))
        c = float(input('Enter third number: '))

        if (a >= b) and (a >= c):
            largest = a

        elif (b >= a) and (b >= c):
            largest = b

        else:
            largest = c

        print("The Largest number is: ", largest)

ln = LargestNumber()
ln.largest_number()

