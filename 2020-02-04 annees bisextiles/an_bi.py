class Year:
    def __init__(self, year):
        self.year = year
        return

    def check_year(self):
        div_4 = self.year % 4
        div_100 = self.year % 100
        div_400 = self.year % 400
        if div_4 == 0 and div_100 != 0:
            return True
        elif div_400 == 0:
            return True
        else:
            return False
       
year = Year(2000)
year2 = Year(1900)
year3 = Year(1993)
year4 = Year(2020)
year5 = Year(2016)
year6 = Year(296)
year7 = Year(-99)

print(year.check_year())
print(year2.check_year())
print(year3.check_year())
print(year4.check_year())
print(year5.check_year())
print(year6.check_year())
print(year7.check_year())

# cls_yr = Year(2007)

