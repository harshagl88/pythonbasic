
class MultipicationTable:

    def multiplication_table(self):
        num = int(input("Enter the number: "))
        for i in range (1, 11):
            print(num, " x ", i, " = ", num * i)

mt = MultipicationTable()
mt.multiplication_table()




