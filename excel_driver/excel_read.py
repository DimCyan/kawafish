import openpyxl
from selenium_library.selenium_keyword import SeleniumKey


def testcase_read(args):
    excel = openpyxl.load_workbook(args.path.name)
    for sheets in excel.sheetnames:
        sheet = excel[sheets]
        for value in sheet.values:
            param = {'name': value[2], 'value': value[3], 'txt': value[4]}
            for key in list(param.keys()):
                if param[key] is None or param[key] == '':
                    del param[key]
            if isinstance(value[0], int):
                if value[1] == 'open_browser':
                    sk = SeleniumKey(param['txt'])
                else:
                    getattr(sk, value[1])(**param)


if __name__ == '__main__':
    testcase_read('../cases/testcase.xlsx')
