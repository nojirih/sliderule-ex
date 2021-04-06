# -*- coding: utf-8 -*-
#  Slide Rule Exercises   ver 1.0
#  Nojiri Housuke
#

import math
import random
import time

Maxproblems = 5
Minlink = 2
Maxlink = 3

print('***** Slide Rule Exercises *****\n')
errave = 0.0
timstart = time.time()
i = 1

while i <= Maxproblems:
    x = random.uniform(1, 100)
    print('({:})\n {:.3f}'.format(i, x))
    m = random.randint(Minlink, Maxlink)
    for j in range(0, m):
        ope = random.choice(('x', '/', 'x', '/', 'sqrt', '**2', 'sin', 'cos', 'tan'))
        if ope == 'x':
            y = random.uniform(1, 100)
            print(' {:.3f} {}'.format(y ,ope))
            x = x * y
        elif ope == '/':
            y = random.uniform(1, 100)
            print(' {:.3f} {}'.format(y ,ope))
            x = x / y
        elif ope == 'sqrt':
            print(' {}'.format(ope))
            x = math.sqrt(x)
        elif ope == '**2':
            print(' {}'.format(ope))
            x = x * x
        elif ope == 'sin':
            y = random.uniform(0, 90)
            print(' sin({:.3f}) *'.format(y))
            x *= math.sin(math.radians(y))
        elif ope == 'cos':
            y = random.uniform(0, 90)
            print(' cos({:.3f}) *'.format(y))
            x *= math.cos(math.radians(y))
        elif ope == 'tan':
            y = random.uniform(0, 90)
            print(' tan({:.3f}) *'.format(y))
            x *= math.tan(math.radians(y))

    sra = float(input('>> ').rstrip())
    error =  (abs(x - sra) / x) * 100

    if error < m:
        errave += error
        print('Excellent!')
        print('True value  {:.3f}    Error  {:.3f}%    Average  {:.3f}%'.format(x, error, errave / i))
        i += 1
    else:
        print('Ooops!')
        print('True value  {:.3f}    Error  {:.3f}%'.format(x, error))

    print("time  {:.1f}".format(time.time() - timstart) + "sec\n")

