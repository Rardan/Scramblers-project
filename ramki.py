from generatory import *
from scramblery import *

def xor(a, b):
    if a != b:
        return 1
    else:
        return 0

class Ramka():
    def __init__(self):
        self.len_ramka = 93
        self.ramka = []
        self.bad = 0

    def loadRamka(self):
        inputF = open('ramka.txt', 'r')
        input = list(map(int, map(str.strip, inputF.readlines())))
        for i in range(0, self.len_ramka):
            self.ramka.append(input[i])
        inputF.close()
    
    def loadData(self):
        inputF = open('ramki\data_de.txt', 'r')
        input = list(map(int, map(str.strip, inputF.readlines())))
        for i in range(0, len(input)):
            self.ramka.append(input[i])
        inputF.close()
       
    def loadSYNC(self):
        self.ramka = []
        inputF = open('ramki\sync.txt', 'r')
        input = list(map(int, map(str.strip, inputF.readlines())))
        for i in range(len(input)):
            self.ramka.append(input[i])
        inputF.close()

    def loadCRC(self):
        inputF = open('ramki\crc.txt', 'r')
        input = list(map(int, map(str.strip, inputF.readlines())))
        for i in range(0, len(input)):
            self.ramka.append(input[i])
        inputF.close()

    def getData(self):
        tab = []
        for i in (7, 54):
            tab.append(self.ramka[i])
        return tab

    def getSYNC(self):
        tab = []
        for i in (0, 7):
            tab.append(self.ramka[i])
        return tab

    def getCRC(self):
        tab = []
        for i in (54, self.len_ramka):
            tab.append(self.ramka[i])
        return tab

    def saveData(self):
        outputF = open('ramki\data.txt', 'w')
        output = []
        for i in range(7, 54):
            output.append(self.ramka[i])
        outputF.write("\n".join(str(x) for x in output))

    def saveSYNC(self):
        outputF = open('ramki\sync.txt', 'w')
        output = []
        for i in range(0, 7):
            output.append(self.ramka[i])
        outputF.write("\n".join(str(x) for x in output))

    def saveCRC(self):
        outputF = open('ramki\crc.txt', 'w')
        output = []
        for i in range(54, self.len_ramka):
            output.append(self.ramka[i])
        outputF.write("\n".join(str(x) for x in output))
    
    def saveRamka(self):
        outputF = open('ramkaa.txt', 'w')
        output = []
        for i in range(0, len(self.ramka)):
            output.append(self.ramka[i])
        outputF.write("\n".join(str(x) for x in output))

    def checkCRC(self, crc):
        
        inputF = open('ramkaa.txt', 'r')

        input = list(map(int, map(str.strip, inputF.readlines())))
        good = True
        for j in range(0, 54):
            if self.ramka[j+7] != 0:
                for k in range(0, 33):
                    self.ramka[j+7+k] = xor(self.ramka[j+7+k], crc[k])

        for i in range(7, len(self.ramka)):
            if self.ramka[i] != 0:
                good = False
        
        if good == False:
            self.bad += 1

        inputF.close()

def checkCRC_1(plik, crc, bad):

    inputF = open(plik, 'r')
    input = list(map(int, map(str.strip, inputF.readlines())))
    good = True

    for j in range(0, 54):
        if input[j+7] != 0:
            for k in range(0, 33):
                input[j+7+k] = xor(input[j+7+k], crc[k])

    print(input)
    for i in range(7, len(input)):
            print(good)
            if input[i] != 0:
                good = False
    
    if good == False:
            bad += 1

    inputF.close()

def bsc(p):
    inputF = open('ramki\data_de.txt', 'r')
    input  = list(map(int, map(str.strip, inputF.readlines())))
    i = 0
    i = random.randint(0, len(input) - 1)
    r = random.randint(1, 10000)
    if r <= p:
        if input[i] == 1:
            input[i] = 0
        else:
                input[i] = 1

    inputF.close()
    outputF = open('ramki\data_de.txt', 'w')
    outputF.write("\n".join(str(x) for x in input))
    outputF.close()

def rameczki():
    gen = Generator()
    crc = gen.generate_crc(33)
    #print(crc)
    #print(len(crc))

    key = []
    key = gen.generate_key(7)


    key2 = []
    key2 = gen.generate_key(43)


    genc = Generator_ramek()
    ram = Ramka()
    x7x6 = X7X6()
    x43 = X43()
    
    print("Podaj ilość ramek do wygenerowania: ")
    x = int(input())


    for i in range(0, x):
        genc.generate(crc)
        ram.loadRamka()
        #print(ram.ramka)
        ram.saveSYNC()
        ram.saveData()
        ram.saveCRC()

        key_1 = []
        key_2 = []
        for i in range(len(key)):
            key_1.append(key[i])
            key_2.append(key[i])

        key2_1 = []
        key2_2 = []
        for i in range(len(key2)):
            key2_1.append(key2[i])
            key2_2.append(key2[i])

        x7x6.scrambler_sync('ramki\data.txt', 'ramki\scr1.txt', key_1)
        x43.scrambler('ramki\scr1.txt', 'ramki\scr2.txt', key2_1)

        x43.descrambler('ramki\scr2.txt', 'ramki\scr1_de.txt', key2_2)
        x7x6.descrambler_sync('ramki\scr1_de.txt', 'ramki\data_de.txt', key_2)

        bsc(10)

        ram.loadSYNC()
        ram.loadData()
        ram.loadCRC()

        ram.saveRamka()
    #    print(ram.ramka)
        ram.checkCRC(crc)

    print('wygenerowano i przesłano %d ramek' % x)
    print('odrzucono %d ramek' % ram.bad)