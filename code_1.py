# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def zipper(listA, listB):
    zipped = zip(listA, listB)
    
    return zipped

if __name__ == '__main__':
    food = ["pizza","sushi","jam", "pho", "tofu"]
    people = ["Bob", "Kevin", "Angela","Meredith","Max"]
    
    result = zipper(food, people)
    for item in result:
        print(item)