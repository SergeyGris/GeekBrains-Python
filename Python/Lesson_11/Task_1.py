from datetime import datetime


class Date:
    def __init__(self, date):
        self.date = date

    @staticmethod
    def date_valid(date):
        try:
            datetime.strptime(date, '%d-%m-%Y')
        except ValueError:
            return False
        return True

    @classmethod
    def create_date(cls, date):
        if cls.date_valid(date):
            day, month, year = date.split('-')
            new_date=f'{int(year)}.{int(month)}.{int(day)}'
            return cls(date=new_date)
        else:
            return 'Неверная дата'

    def __str__(self):
        return self.date
        # return f'{self.year}.{self.month}.{self.day}'

lst_date = ["31-12-2021", "32-12-2022", "12-12&##x2013;2022" ]
for date in lst_date:
    rez=Date.create_date(date)
    print(f'Дата: {date}, результат: {rez}')