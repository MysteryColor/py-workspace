# coding=utf-8
import xlrd


class ExcelReader():
    @classmethod
    def read_test(cls, params):
        print
        params

    @staticmethod
    def read_test_static(params):
        print
        params

    def openxls(self):
        return xlrd.open_workbook("C:\\Users\\12981\\Desktop\\桌面整理\\交易流程 (1).xlsx")

if __name__ == '__main__':
    workbook = ExcelReader().openxls()
    sheetsrange=range(workbook.nsheets)
    worksheet = workbook.sheets()[0]
    num_row = worksheet.nrows
    for curren_row in range(num_row):
            row = worksheet.row_values(curren_row)
            print('it`s curren_row content: ', row)
