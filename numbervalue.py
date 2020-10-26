class NumberValue:

    def number_value(self):

        num = int(input("Enter the number: "))

        if num >= 1:
            print("Number is positive")

        elif num <= -1:
            print("number is negative")

        else:
            print("Number value is Zero")

nv = NumberValue()
nv.number_value()