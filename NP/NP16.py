#!/usr/bin/env python3
# @author 轩辕龙儿
# @date 2022/10/26
# @file NP16.py
list = ["Allen", "Tom"]
for i in list:
    print(
        "{}, you have passed our interview and will soon become a member of our company.".format(
            i
        )
    )
list.remove("Tom")
list.append("Andy")
for i in list:
    print("{}, welcome to join us!".format(i))
