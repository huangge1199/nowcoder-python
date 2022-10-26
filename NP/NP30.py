#!/usr/bin/env python3
# @author 轩辕龙儿
# @date 2022/10/26
# @file NP30.py

def solution():
    num = int(input())
    queue = [1, 2, 3, 4, 5]
    queue.pop(0)
    print(queue)
    queue.pop(0)
    print(queue)
    queue.append(num)
    print(queue)


if __name__ == "__main__":
    solution()
