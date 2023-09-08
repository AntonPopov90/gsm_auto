import openpyxl
import calendar
from check_file import cheque_verify


excel_file = 'gsm.xlsx'
check_file = 'check.jpg'
wb = openpyxl.load_workbook(excel_file)
sheet = wb.active


def calculate_distance(cheque_data: dict) -> int:
    if type(cheque_data) is not dict:
        return 'error'
    else:
        sum = int(cheque_data['sum'])
        distance = int((sum/45.9)/0.11)
        return distance


print(calculate_distance(cheque_verify(check_file)))


def fill_dates(cheque_data: dict) -> None:
    """get date in check and fill workdays dates in excel file"""
    if type(cheque_data) is not dict:
        return 'error'
    else:
        year = cheque_data['date'].year  # get year from cheque
        month = cheque_data['date'].month  # get month from cheque

        k = 0
        first_cell = 10  # cell with first date       
        for day in range(1, 32):
            try:
                weekday = calendar.weekday(year, month, day)
            except ValueError:
                continue
            if weekday < calendar.SATURDAY:
                first_cell += 1
                date = f'A{first_cell}'
                distance_cell = f'D{first_cell}'
                fuel_consumption = f'E{first_cell}'
                fuel_price = f'F{first_cell}'
                k += 1
                sheet[date] = "%02d.%02d.%d" % (day, month, year)
                sheet[fuel_consumption] = 0.11
                sheet[fuel_price] = 45.9
                wb.save('gsm.xlsx')  # fill dates

        everyday_distance = int(calculate_distance(cheque_verify(check_file))/k)
        for i in range(11, k+11):
            distance_cell = f'D{i}'
            sheet[distance_cell] = everyday_distance
        
        wb.save('gsm.xlsx')
        
        return 'all right'


print(fill_dates(cheque_verify(check_file)))


def write_to_excel():
    pass
