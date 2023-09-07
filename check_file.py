from datetime import datetime
from pyzbar import pyzbar
import cv2


def cheque_verify(filename: str) -> str or dict:
    """try to find qrcode in file and decode it"""
    if filename.lower().endswith(('.png', '.jpg', '.jpeg')):  # checking file
        img = cv2.imread(filename)  # read QR code
        qrcodes = pyzbar.decode(img)
        if len(qrcodes) > 0:
            try:  # prepare dict with datetime and sum
                parsed_list = str(qrcodes).split('&')  # convert to string
                date = parsed_list[0].split("'")[1][2:]  # string with date
                date_format = "%Y%m%dT%H%M"
                datetime_obj = datetime.strptime(date, date_format)
                sum = float(parsed_list[1][2:])  # get sum from cheque
                result_dict = {'date': datetime_obj, 'sum': sum}
                return result_dict
            except ValueError:
                return str('Похоже вы прислали чек не с АЗС')
        else:
            return str('Не удалось распознать чек, попробуйте еще раз')
    else:
        return str("Загруженный формат изображения не поддерживается.\n"
                   "Форматы: png, jpg, jpeg")
