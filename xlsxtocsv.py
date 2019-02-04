from openpyxl import load_workbook
import csv

wb = load_workbook(filename='sukunimet.xlsx')

with open('sukunimet.csv', mode='w', encoding="UTF-8") as filu:
    filu = csv.writer(filu, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    sheet_ranges = wb['Nimet']
    a = 1
    while a <= 22691:
        nimi = 'A' + str(a)
        lkm = 'B' + str(a)
        print(sheet_ranges[nimi].value, sheet_ranges[lkm].value)
        filu.writerow([sheet_ranges[nimi].value, sheet_ranges[lkm].value])
        a += 1
