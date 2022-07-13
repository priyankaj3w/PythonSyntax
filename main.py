# This is a sample Python script.
import sys


def print_hi(name):
    print(f'Hi, {name}')


def working_with_list():
    x = 'Priyanka'
    y = x[::-1]
    sys.stdout.write('Original:' + x + '\n')
    print('Reverse:' + y)


def working_with_dict():
    tiny_dict = {'name': 'john', 'code': 6734, 'dept': 'sales'}
    print(tiny_dict)
    print(tiny_dict.keys())
    print(tiny_dict.values()) (union bnak of indai, bank of baroda, HDFC and Kotak)


if __name__ == '__main__':
    print_hi("Okay")
    working_with_list()
    working_with_dict()
