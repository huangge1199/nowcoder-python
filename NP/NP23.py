#!/usr/bin/env python3
# @author 轩辕龙儿
# @date 2022/10/26
# @file NP23.py

def solution():
    name = input().split()
    name.remove(input())
    print(name)


if __name__ == "__main__":
    solution()
