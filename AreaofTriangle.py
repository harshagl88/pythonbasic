

class AresOfTriagnle:

    def area_triangle(self):

        a = float(input('Enter first side: '))
        b = float(input('Enter second side: '))
        c = float(input('Enter third side: '))

        p = (a + b + c) /2

        area = (p*(p-a)*(p-b)*(p-c)) ** 0.5
        print("Area of the triangle is: " + str(area))

aot = AresOfTriagnle()
aot.area_triangle()