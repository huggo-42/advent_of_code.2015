import hashlib
import time
import os
start = time.time()
os.system('clear')
print('=-' * 29 + '=')
print('Running...\n')

secretKeyPrefix = 'yzbqklnj'
counter = 0

while (True):
    str2hash = secretKeyPrefix + str(counter)
    hexResult = hashlib.md5(str2hash.encode()).hexdigest()

    if hexResult[0: 6] == '000000':
        print('hexResult: ' + str(hexResult))
        print('secretKey: ' + str2hash)
        print('answer: ' + str(counter))
        break
    else:
        counter += 1

print('-' * 35 + '\nExecution time: ' + str(time.time() - start))
