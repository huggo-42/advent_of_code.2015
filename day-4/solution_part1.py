import hashlib
import os
import time

start = time.time()
os.system('clear')
print('=-' * 29 + '=')

strings = open("input.data", "r").readlines()

niceStrings = 0

for string in strings:
    firstValidation = False
    secondValidation = False
    thirdValidation = True

    a = string.count('a')
    e = string.count('e')
    i = string.count('i')
    o = string.count('o')
    u = string.count('u')
    if a + e + i + o + u >= 3:
        firstValidation = True

    for idx in range(0, len(string) - 1, 2):
        if string[idx] == string[idx + 1]:
            # print('string[idx] == string[idx + 1] => ' + str(string[idx] == string[idx + 1]))
            subString = str(string[idx] + ' -> ' + string[idx + 1])
            secondValidation = True
            break

    cantContainStringList = ['ab', 'cd', 'pq', 'xy']
    resultant_str = any(x in string for x in cantContainStringList)

    if resultant_str:
        thirdValidation = False

    if firstValidation == True and secondValidation == True and thirdValidation == True:
        # print(string)
        # print(string.count('a'))
        # print(string.count('e'))
        # print(string.count('i'))
        # print(string.count('o'))
        # print(string.count('u'))
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        print('string: ' + str(string))
        print('a + e + i + o + u >= 3 = ' + str(a + e + i + o + u >= 3))
        print('subString' + str(subString))
        print('cantContainStringList: ' + str(cantContainStringList))
        print('resultant_str: ' + str(resultant_str))
        print('[[GOOD ONE]]')
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        niceStrings += 1

print(str(niceStrings) + ' strings are nice, Santa!')

print('-' * 35 + '\nExecution time: ' + str(time.time() - start))
print('=-' * 29 + '=')
