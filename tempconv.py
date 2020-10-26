class TempConv:

    def celtoft(self):

        celcius = float(input("Enter the celcius: "))

        fahrenheit = (celcius * 1.8) + 32

        print("%0.2f celcius is equal to %0.2f fahrenheit" %(celcius, fahrenheit))


    def fttocel(self):

        fahrenheit = float(input("Enter the fahrenheit: "))

        celcius = (fahrenheit - 32) / 1.8

        print("%0.2f fahrenheit is equal to %0.2f celcius" %(fahrenheit, celcius))




tc = TempConv()
tc.celtoft()
tc.fttocel()