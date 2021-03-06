import argparse
from excel_driver.excel_read import testcase_read

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=
        '''π π π π π π π π π π πγγγFISHING γγγπ π π π π π π π π π π π π ''')
    parser.add_argument(
        '--path',
        type=argparse.FileType(
            'r',
            encoding='UTF-8'),
        required=True,
        help='Testcase(.xlsx) Path')
    args = parser.parse_args()
    testcase_read(args)
    args.path.close()
