
#!/usr/bin/env python
# coding=utf-8
import random


def gener_code(code_len=4):
    all = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    last_len = len(all) - 1
    code = ''
    for _ in range(code_len):
        index = random.randint(0, last_len)
        # index = randint(1, 10)
        code += all[index]
    print(code)
    return code


if __name__ == "__main__":
    gener_code()
