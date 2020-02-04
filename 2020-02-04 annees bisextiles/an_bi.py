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


# cls_yr = Year(2007)
