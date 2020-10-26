class ConvkiloMiles:

    def conv_kilo_miles(self):

        kilometer = float(input("Enter the kilometer: "))

        miles = kilometer * 0.621

        print("%0.2f kilometer is equal to %0.2f miles" %(kilometer, miles))

    def conv_miles_kilo(self):

        miles = float(input("Enter the miles: "))

        kilometer = miles/0.621

        print("%0.2f miles is equal to %0.2f kilometers" %(miles, kilometer))

ckm = ConvkiloMiles()
ckm.conv_miles_kilo()
ckm.conv_kilo_miles()
