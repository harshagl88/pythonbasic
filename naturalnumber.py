class NaturalNumber:

    def natural_number(self):
        num = int(input("Enter the number: "))

        sum = 0
        while (num > 0):
            sum = sum + num

            num = num - 1
        print(sum)


nn = NaturalNumber()
nn.natural_number()
