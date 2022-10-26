#!/usr/bin/env python3
# @author 轩辕龙儿
# @date 2022/10/26
# @file NP28.py

def solution():
    # num1 = input()
    # num2 = []
    # for i in range(len(num1)):
    #     num2.append((int(num1[i]) + 3) % 9)
    # num2[0], num2[2] = num2[2], num2[0]
    # num2[1], num2[3] = num2[3], num2[1]
    # for i in num2:
    #     print(i, end="")

    s = input()
    print("".join(str((int(num) + 3) % 9) for num in (s[2], s[3], s[0], s[1])))


if __name__ == "__main__":
    solution()
