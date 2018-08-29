from generatory import *
from scramblery import *
from statystyka import *
from ramki import *
from test import *
import os


def menu_scr():
    gene = Generator()
    os.system('CLS')
    print('1. Wygeneruj dane wejściowe')
    print('2. Scrambler DVB (s)')
    print('3. Scrambler V.34 (as)')
    print('4. Scrambler x7+x6+1 (s)')
    print('5. Scrambler x43+1 (as)')
    print('6. Scrambler x16+1 (s)')
    print('7. Scrambler x24+x22+1 (as)')
    print('8. Powrót')
    select = input()

    if select == '1':
        os.system('CLS')
        st = Statystyka()  
        print('Podaj liczbe bitów: ')
        x = int(input())
        gene.generate(x)            
        st.stat_wykres('input')
        st.count('input')
        plt.show()

    elif select == '2':
        dvb = DVB()
        st = Statystyka()
        key = []
        key = gene.generate_key(15)
        key_1 = []
        for i in range(len(key)):
            key_1.append(key[i])
        dvb.scrambler('input.txt', 'outputDVB.txt', key)
        dvb.descrambler('outputDVB.txt', 'outputDVB_de.txt', key_1)
        st.stat_wykres('DVB')
        st.count('DVB')
        plt.show()


    elif select == '3':
        v34 = V34()
        st = Statystyka()
        key = []
        key = gene.generate_key(23)
        key_1 = []
        for i in range(len(key)):
            key_1.append(key[i])
        v34.scrambler('input.txt','outputV34.txt',key)
        v34.descrambler('outputV34.txt','outputV34_de.txt',key_1)
        st.stat_wykres('V34')
        st.count('V34')
        plt.show()

    elif select == '4':
        x7x6 = X7X6()
        st = Statystyka()
        key = []
        key = gene.generate_key(7)
        key_1 = []
        for i in range(len(key)):
            key_1.append(key[i])
        x7x6.scrambler('input.txt', 'outputx7x6.txt', key)
        x7x6.descrambler('outputx7x6.txt', 'outputx7x6_de.txt', key_1)
        st.stat_wykres('x7x6')
        st.count('x7x6')
        plt.show()

    elif select == '5':
        x43 = X43()
        st = Statystyka()
        key = []
        key = gene.generate_key(43)
        key_1 = []
        for i in range(len(key)):
            key_1.append(key[i])
        x43.scrambler('input.txt', 'outputx43.txt', key)
        x43.descrambler('outputx43.txt', 'outputx43_de.txt', key_1)
        st.stat_wykres('x43')
        st.count('x43')
        plt.show()

    elif select == '6':
        x16 = X16()
        st = Statystyka()
        key = []
        key = gene.generate_key(16)
        key_1 = []
        for i in range(len(key)):
            key_1.append(key[i])
        x16.scrambler('input.txt', 'outputx16.txt', key)
        x16.descrambler('outputx16.txt', 'outputx16_de.txt', key_1)
        st.stat_wykres('x16')
        st.count('x16')
        plt.show()

    elif select == '7':
        x24x22 = X24X22()
        st = Statystyka()
        key = []
        key = gene.generate_key(24)
        key_1 = []
        for i in range(len(key)):
            key_1.append(key[i])
        x24x22.scrambler('input.txt', 'outputx24x22.txt', key)
        x24x22.descrambler('outputx24x22.txt', 'outputx24x22_de.txt', key_1)
        st.stat_wykres('x24x22')
        st.count('x24x22')
        plt.show()
        
    elif select == '8':
        print('Wracam')
        return
    else:
        print('Błędny wybór')