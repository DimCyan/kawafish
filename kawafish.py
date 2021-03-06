import argparse
from excel_driver.excel_read import testcase_read

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=
        '''𓆝 𓆟 𓆜 𓆞 𓆝 𓆟 𓆜 𓆞 𓆝 𓆟 𓆜。。。FISHING 。。。𓆞 𓆝 𓆟 𓆜 𓆞 𓆝 𓆟 𓆜 𓆞 𓆝 𓆟 𓆜 𓆞 ''')
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
