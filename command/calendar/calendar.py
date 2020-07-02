from .. import Command
import datetime
from poppo.lib import explorer

class Calendar(Command):
    def __init__(self, options, argv):
        self.argv = argv
        return
    
    def exec(self):
        if len(self.argv) > 1:
            print("too many arguments.")
            return

        try:
            m = int(self.argv[0]) if self.argv else 0
        except:
            print("invalid argument.")
            return
             
        calendar_template = open(f"{__file__}/../calendar_template.html", encoding="utf-8").read()

        if m:
            user_date = datetime.date(datetime.datetime.today().year, m, 1)
        else:
            user_date = datetime.datetime.today()

        formatted_calendar = calendar_template.format(*map(convert_date_row, calendar_rows(user_date)))

        open(f"{__file__}/../calendar.html", "w", encoding="utf-8").write(formatted_calendar)
        explorer.open(f"{__file__}\..\calendar.html")

def calendar_rows(user_date: datetime.datetime = None):
    """
    カレンダーの行(日曜日はじめ)を取得するジェネレータ

    Args:
        user_date (datetime.datetime): 任意の日時。その日時が属するカレンダーを取得する。デフォルトは今日。

    Yields:
        List[datetime.datetime]: カレンダーの行
    """
    if not user_date:
        user_date = datetime.datetime.today()
    first_date = datetime.date(user_date.year, user_date.month, 1)
    first_weekday = first_date.isoweekday()

    last_monthdays = [first_date - datetime.timedelta(days=i) for i in range(first_weekday, 0, -1)]
    
    first_week = last_monthdays + [first_date + datetime.timedelta(days=i) for i in range(7 - first_weekday)]
    
    for i in range(6):
        yield [date + datetime.timedelta(days=i*7) for date in first_week]

def convert_date_row(date_row):
    return "".join(f'<td id="{date.year}-{date.month:02}-{date.day:02}" class="{"holiday" if i == 0 else ""}">{date.day:02}</td>' for i, date in enumerate(date_row))


