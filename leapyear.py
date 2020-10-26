class LeapYear:

    def leap_year(self):

        year = int(input("Enter the Year: "))

        if (year % 4) == 0:
            if (year % 100) == 0:
                if (year % 400) == 0:
                    print("{0} is leap year".format(year))
                else:
                    print("{0} is not leap year".format(year))

            else:
                print("{0} is leap year".format(year))

        else:
            print("{0} is not leap year".format(year))

ly = LeapYear()
ly.leap_year()

