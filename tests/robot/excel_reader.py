import openpyxl

def read_excel_data(file_path):
    workbook = openpyxl.load_workbook(r'C:\Users\ycycr\project-chiru\tests\robot\excel_data.xlsx', 'r'
    sheet = workbook.active
    data = []

    for row in sheet.iter_rows(min_row=2, values_only=True):
        data.append(list(row))

    return data
