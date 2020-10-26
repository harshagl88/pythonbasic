

class ArmStrong:

    def armstrong_number(self):

        num1 = int(input("Enter the lower number: "))
        num2 = int(input("Enter the upper number: "))

        for num in range(num1, num2 + 1):

            order = len(str(num))
            sum = 0
            temp = num
            while temp > 0:
                digit = temp % 10
                sum = sum + (digit ** order)
                temp = temp // 10
            if num == sum:
                print(num)


ast = ArmStrong()
ast.armstrong_number()



