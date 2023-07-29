import hashlib
import os
import time
start = time.time()
os.system('clear')
print('=-' * 29 + '=')

secretKeyPrefix = 'yzbqklnj'
counter = 282750

while (True):
    str2hash = secretKeyPrefix + str(counter)
    hexResult = hashlib.md5(str2hash.encode()).hexdigest()

    if hexResult[0: 5] == '00000':
        print('hexResult: ' + str(hexResult))
        print('secretKey: ' + str2hash)
        print('answer: ' + str(counter))
        break
    else:
        counter += 1

print('-' * 35 + '\nExecution time: ' + str(time.time() - start))
print('=-' * 29 + '=')
