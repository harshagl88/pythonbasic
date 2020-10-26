class SwapVariable:

    def swap_with_variable(self):

        a = input('Enter first variable: ')
        b = input('Enter second variable: ')

        temp = a
        a = b
        b = temp

        print("The value of a after swapping: " + str(a))
        print("The value of b after swapping: " + str(b))

     # With out creating new variable

    def swap_without_variable(self):

        a = int(input('Enter first variable: '))
        b = int(input('Enter second variable: '))

        a = a + b
        b = a - b
        a = a - b

        print("The value of a after swapping: " + str(a))
        print("The value of b after swapping: " + str(b))



sv = SwapVariable()
sv.swap_without_variable()




