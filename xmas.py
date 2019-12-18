import colorama
import random
from os import system, name 
from time import sleep 
def clear(): 
    if name == 'nt': #windows
        _ = system('cls') 
colorama.init()
slist=['0', '1']
clist = ['\033[0;31m', '\033[0;32m', '\033[1;33m', '\033[0;34m', '\033[1;37m']
wcolor = '\033[0;33m'
num = int(input("Sorok száma: "))
m = num
l = ['0', '1']
while True:
    clear()
    for i in range(0, num):
        pattern = ' ' * num
        if i==0:
            pattern = ''
        print(pattern, end='')
        for z in range(0, i):
            rc = [random.randint(0,len(slist) - 1), random.randint(0,len(slist) - 1), random.randint(0, len(clist) - 1), random.randint(0, len(clist) - 1)]
            print(clist[rc[2]] + slist[rc[0]] + clist[rc[3]] + slist[rc[1]], end='')
            if z == i - 1:
                print('')
        if i == m - 1:
            pattern = ' '
            if m < 10:
                print(pattern * (i) + wcolor + '||')
            else:
                for j in range(0, round(m/4)):
                    print(pattern * (i) + wcolor + '||')
        num -= 1
    num = m
    sleep(.1)