import openpyxl
import calendar
from check_file import cheque_verify 


excel_file = 'gsm.xlsx'
check_file = 'check.jpg'
wb = openpyxl.load_workbook(excel_file)
sheet = wb.active


def fill_dates(cheque_data: dict) -> None:
    """get date in check and fill workdays dates in excel file"""
    if type(cheque_data) is not dict:
        return 'error'
    else:
        year = cheque_data['date'].year  # get year from cheque
        month = cheque_data['date'].month  # get month from cheque

        k = 0
        date_cell = 10  # cell of first date
        for day in range(1, 32):
            try:
                weekday = calendar.weekday(year, month, day)
            except ValueError:
                continue
            if weekday < calendar.SATURDAY:
                date_cell += 1
                x = f'A{date_cell}'
                k += 1
        # format the result
                sheet[x] = "%02d.%02d.%d" % (day, month, year)  # fill dates
        wb.save('gsm.xlsx')
        return 'all right'


print(fill_dates(cheque_verify(check_file)))


def write_to_excel():
    pass
