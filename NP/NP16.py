#!/usr/bin/env python3
# @author 轩辕龙儿
# @date 2022/10/26
# @file NP16.py

def solution():
    nameList = ["Allen", "Tom"]
    for i in nameList:
        print(
            "{}, you have passed our interview and will soon become a member of our company.".format(
                i
            )
        )
    nameList.remove("Tom")
    nameList.append("Andy")
    for i in nameList:
        print("{}, welcome to join us!".format(i))


if __name__ == "__main__":
    solution()
