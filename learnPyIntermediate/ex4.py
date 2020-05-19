import sys

def check_help_keyword(argv_list):
    if '--help' in argv_list or '-h' in argv_list:
        return True
    else:
        return False

if check_help_keyword(sys.argv):
    print('manual description!')
print(sys.argv)