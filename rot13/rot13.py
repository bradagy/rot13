#!/usr/bin/env python3


import string


def encrypt(text, n):
    in_tab = string.ascii_lowercase
    out_tab = in_tab[n % 26:] + in_tab[:n % 26]
    trans_tab = str.maketrans(in_tab, out_tab)

    return text.translate(trans_tab)


def rot13():
    while True:
        user_input = input('Please enter the text here: ')
        if not user_input.isalpha():
            print('The input you entered was not correct. Numbers are also '
                  'not accepted. Please try again.')
            continue
        else:
            print(f"The encryption is {encrypt(user_input, 13)}.")
            break


rot13()
