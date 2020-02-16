import datetime

class Date:

    DAY_OF_MONTH = ((31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31),  # not leap year
                    (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31))  # leap year


    def __init__(self, *args):
        '''
        Examples:
            Format day: от 1 до количество дней в данном месяце и году
            Format month: от 1 до 12
            Format year: от 1000 до 9999
            d1 = Date(2020, 1, 1)       # 2020.01.01
            d2 = Date('2020.01.01')     # 2020.01.01
            d_default = Date()          # 1970.01.01
        Exception:
            TypeError('Arguments must be in the next format: year - int, month - int, day - int or "YYYY.MM.DD"')
            ValueError('year must be 1000 <= year <= 9999')
            ValueError('month must be 1 <= month <= 12')
            ValueError('day must be 1 <= day <= количество дней в данном месяце и году')
        '''
        self.year, self.month, self.day = self.__is_valid_date(*args)


    def __str__(self):
        year = str(self.year)
        month = str(self.month) if self.month > 9 else f'0{self.month}'
        day = str(self.day) if self.day > 9 else f'0{self.day}'
        return f'{year}.{month}.{day}'

    def __repr__(self):
        return f"Date('{self.__str__()}')"

    @staticmethod
    def is_leap_year(year):
        if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
            return False
        else:
            return True

    @classmethod
    def get_max_day(cls, year, month):
        leap_year = 1 if cls.is_leap_year(year) else 0
        return cls.DAY_OF_MONTH[leap_year][month-1]

    @property
    def date(self):
        return self.__str__()

    @classmethod
    def __is_valid_date(cls, *args):
        if not args:
            cls.year = 1970
            cls.month = 1
            cls.day = 1
            return cls.year, cls.month, cls.day
        try:
            if len(args) == 1 and isinstance(args[0], str):
                date = args[0].split('.')
                if len(date) != 3:
                    raise Exception()
                cls.year = int(date[0])
                cls.month = int(date[1])
                cls.day = int(date[2])
                leap_year = 1 if cls.is_leap_year(cls.year) else 0
                if not 1000 <= cls.year <= 9999:
                    raise ValueError('year must be 1000 <= year <= 9999')
                if not 1 <= cls.month <= 12:
                    raise ValueError('month must be 1 <= month <= 12')
                if not 1 <= cls.day <= cls.DAY_OF_MONTH[leap_year][cls.month-1]:
                    raise ValueError('day must be 1 <= day <= количество дней в данном месяце и году')
                return cls.year, cls.month, cls.day
            if len(args) == 3:
                cls.year = args[0]
                cls.month = args[1]
                cls.day = args[2]
                leap_year = 1 if cls.is_leap_year(cls.year) else 0
                if not isinstance(cls.year, int):
                    raise Exception()
                if not isinstance(cls.month, int):
                    raise Exception()
                if not isinstance(cls.day, int):
                    raise Exception()

                if not 1000 <= cls.year <= 9999:
                    raise ValueError('year must be 1000 <= year <= 9999')
                if not 1 <= cls.month <= 12:
                    raise ValueError('month must be 1 <= month <= 12')
                if not 1 <= cls.day <= cls.DAY_OF_MONTH[leap_year][cls.month-1]:
                    raise ValueError('day must be 1 <= day <= количество дней в данном месяце и году')
                return cls.year, cls.month, cls.day
        except:
            raise TypeError('Arguments must be in the next format: year - int, month - int, day - int or "YYYY.MM.DD"')

    @date.setter
    def date(self, value):
        self.__init__(value)

    @property
    def day(self):
        return f'{self.day}'

    @property
    def month(self):
        return f'{self.month}'

    @property
    def year(self):
        return f'{self.year}'

    def add_day(self, day):
        if not isinstance(day, int):
            raise TypeError('Argument day must be int')
        if day < 0:
            raise ValueError('Argument day must be positive or zero')
        leap_year = 1 if self.is_leap_year(self.year) else 0
        day_in_month = self.DAY_OF_MONTH[leap_year][self.month-1]
        self.add_month(day//day_in_month)
        day = day % day_in_month
        if self.day + day > self.DAY_OF_MONTH[leap_year][self.month-1]:
            self.add_month(1)
            day -= self.DAY_OF_MONTH[leap_year][self.month-1]
        self.day += day


    def add_month(self, month):
        if not isinstance(month, int):
            raise TypeError('Argument month must be int')
        if month < 0:
            raise ValueError('Argument month must be positive or zero')
        self.add_year(month//12)
        month = month % 12
        if self.month + month > 12:
            self.add_year(1)
            month -= 12
        self.month += month


    def add_year(self, year):
        if not isinstance(year, int):
            raise TypeError('Argument year must be int')
        if year < 0:
            raise ValueError('Argument year must be positive or zero')
        self.year += year


    @staticmethod
    def date2_date1(date2, date1):
        '''
        Format date1 and date2: tuple(int, int, int)
        d = Date()
        d.date2_date1((2020,1,1),(2019,1,1))    # 365 days
        '''
        data2 = datetime.datetime(date2[0], date2[1], date2[2])
        data1 = datetime.datetime(date1[0], date1[1], date1[2])
        delta = data2 - data1
        return f'{abs(delta.days)} days'



