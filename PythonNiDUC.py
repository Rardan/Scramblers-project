from generatory import *
from scramblery import *
from statystyka import *
from ramki import *
from test import *
from menu import *
import os

test2()


while True:
        print('NiDUC – grupa 8.')
        print('1. Scramblery')
        print('2. Test ramek')
        print('3. Skład grupy')
        print('4. Zakoncz')
        select = input()

        if select == '1':
            os.system('CLS')
            menu_scr()
            os.system('CLS')

        elif select == '2':
            os.system('CLS')
            rameczki()
            x = input()
            os.system('CLS')

        elif select == '3':
            os.system('CLS')
            print('Przemysław Skoneczny – 234946')
            print('Piotr Pawelski – 218370')
            print('Szymon Bodziony – 208343\n')

        elif select == '4':
            break

        else:
            os.system('CLS')
            print('Błędny wybór')





    
