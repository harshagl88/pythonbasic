class OddEven:

    def check_odd_even(self):

        num = int(input("Enter the number: "))

        remainder = num % 2

        if remainder == 0 :
            print("Number is Even")

        else:
            print("Number is odd")

oe = OddEven()
oe.check_odd_even()

