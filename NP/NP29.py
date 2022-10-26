#!/usr/bin/env python3
# @author 轩辕龙儿
# @date 2022/10/26
# @file NP29.py

def solution():
    num = int(input())
    stack = [1, 2, 3, 4, 5]
    stack.pop()
    print(stack)
    stack.pop()
    print(stack)
    stack.append(num)
    print(stack)


if __name__ == "__main__":
    solution()
