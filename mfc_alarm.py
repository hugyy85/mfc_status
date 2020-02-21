import requests
from tkinter import *


def show_status_mfc(check_code: str) -> str:
    url = f'https://www.mfc-nso.ru/api/v1/data/requests/{check_code}'
    response = requests.get(url).json()
    status = response['data']['status']
    comment = response['data']['comment']
    with open('mfc_status', 'r', encoding='utf-8') as f:
        old_status = f.read()

    if old_status != status:
        with open('mfc_status', 'w', encoding='utf-8') as f:
            f.write(status)
        result = f'Статус изменился с "{old_status}" на "{status}": {comment}'
    else:
        return 'false'
    root = Tk()

    text = Text(width=50, height=10)
    text.pack()
    text.insert(1.0, result)

    text.tag_add('title', 1.0, '1.end')
    text.tag_config('title', font=("Verdana", 15, 'bold'), justify=CENTER)

    root.mainloop()

    return result


show_status_mfc('5714495')


