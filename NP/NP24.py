#!/usr/bin/env python3
# @author 轩辕龙儿
# @date 2022/10/26
# @file NP24.py

def solution():
    names = input().split()
    del names[-3:]
    print(names)


if __name__ == "__main__":
    solution()
