#!/usr/bin/env python3

import io
import sys

def print_fibonacci(length):
    fibonacci_list = [] 

    
    if length >= 1:
        fibonacci_list.append(0)
    if length >= 2:
        fibonacci_list.append(1)
    for i in range(2, length):
        fibonacci_list.append(fibonacci_list[i - 1] + fibonacci_list[i - 2])

    print(str(fibonacci_list))

def test_print_fibonacci_zero(self):
    '''prints empty list when length = 0'''
    captured_out = io.StringIO()
    sys.stdout = captured_out
    print_fibonacci(0)
    sys.stdout = sys.__stdout__
    assert captured_out.getvalue() == '[]\n'

def test_print_fibonacci_one(self):
    '''prints [0] when length = 1'''
    captured_out = io.StringIO()
    sys.stdout = captured_out
    print_fibonacci(1)
    sys.stdout = sys.__stdout__
    assert captured_out.getvalue() == '[0]\n'

def test_print_fibonacci_two(self):
    '''prints [0, 1] when length = 2'''
    captured_out = io.StringIO()
    sys.stdout = captured_out
    print_fibonacci(2)
    sys.stdout = sys.__stdout__
    assert captured_out.getvalue() == '[0, 1]\n'
