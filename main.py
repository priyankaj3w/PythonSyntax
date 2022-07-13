# This is a sample Python script.
import sys
import loops


def print_hi(name):
    print(f'Hi, {name}')


def working_with_list():
    x = 'Priyanka'
    y = x[::-1]
    sys.stdout.write('Original:' + x + '\n')
    print('Reverse:' + y)


def working_with_list():
    var_tuple = ('apple', 'mango', 'guava', 'orange', 'banana', 'cherry')
    tiny_tuple = (123, 'john')
    print('Tuple is:')
    print(var_tuple+tiny_tuple)
    loops.for_loop(var_tuple)


def working_with_dict():
    tiny_dict = {'name': 'john', 'code': 6734, 'dept': 'sales'}
    print('Dictionary is:')
    print(tiny_dict)
    print(tiny_dict.keys())
    print(tiny_dict.values())


def decision_making(a, b):
    if a > b:
        print('a is greater')
    else:
        print('b is greater')


if __name__ == '__main__':
    print_hi("Okay")
    working_with_list()
    working_with_dict()
    decision_making(4, 10)
