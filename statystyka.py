import matplotlib.pyplot as plt
import numpy
class Statystyka:

    def __init__(self):
        self.hist = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.index = ['00', '11', '000', '111', '0000', '1111', '00000', '11111', '000000', '111111','0000000', '1111111','00000000', '11111111', '000000000', '111111111', '0000000000', '1111111111']
        self.p_i = [pow(1/2,2), pow(1/2,2), pow(1/2,3), pow(1/2,3), pow(1/2,4), pow(1/2,4), pow(1/2,5), pow(1/2,5), pow(1/2,6), pow(1/2,6), pow(1/2,7), pow(1/2,7), pow(1/2,8), pow(1/2,8), pow(1/2,9), pow(1/2,9), pow(1/2,10), pow(1/2,10)]

    def stat(self, plik, key):
        stat = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        # stat[0] -> 00
        # stat[1] -> 11
        # stat[2] -> 000
        # stat[3] -> 111
        # stat[4] -> 0000
        # stat[5] -> 1111
        # stat[6] -> 00000
        # stat[7] -> 11111
        # stat[8] -> 000000
        # stat[9] -> 111111
        # stat[10] -> 0000000
        # stat[11] -> 1111111
        # stat[12] -> 00000000
        # stat[13] -> 11111111

        inputF = open(plik, 'r')
        input = list(map(int, map(str.strip, inputF.readlines())))

        for i in range(0, len(input)):
            if i >= 1:
                if input[i-1] == input[i] == 0:
                    stat[0] += 1
                    self.hist[0] += 1
                if input[i-1] == input[i] == 1:
                    stat[1] += 1
                    self.hist[1] += 1
            if i >= 2:
                if input[i-2] == input[i-1] == input[i] == 0:
                    stat[2] += 1
                    self.hist[2] += 1
                if input[i-2] == input[i-1] == input[i] == 1:
                    stat[3] += 1
                    self.hist[3] += 1
            if i >= 3:
                if input[i-3] == input[i-2] == input[i-1] == input[i] == 0:
                    stat[4] += 1
                    self.hist[4] += 1
                if input[i-3] == input[i-2] == input[i-1] == input[i] == 1:
                    stat[5] += 1
                    self.hist[5] += 1
            if i >= 4:
                if input[i-4] == input[i-3] == input[i-2] == input[i-1] == input[i] == 0:
                    stat[6] += 1
                    self.hist[6] += 1
                if input[i-4] == input[i-3] == input[i-2] == input[i-1] == input[i] == 1:
                    stat[7] += 1
                    self.hist[7] += 1
            if i >= 5:
                if input[i-5] == input[i-4] == input[i-3] == input[i-2] == input[i-1] == input[i] == 0:
                    stat[8] += 1
                    self.hist[8] += 1
                if input[i-5] == input[i-4] == input[i-3] == input[i-2] == input[i-1] == input[i] == 1:
                    stat[9] += 1
                    self.hist[9] += 1
            if i >= 6:
                if input[i-6] == input[i-5] == input[i-4] == input[i-3] == input[i-2] == input[i-1] == input[i] == 0:
                    stat[10] += 1
                    self.hist[10] += 1
                if input[i-6] == input[i-5] == input[i-4] == input[i-3] == input[i-2] == input[i-1] == input[i] == 1:
                    stat[11] += 1
                    self.hist[11] += 1
            if i >= 7:
                if input[i-7] == input[i-6] == input[i-5] == input[i-4] == input[i-3] == input[i-2] == input[i-1] == input[i] == 0:
                    stat[12] += 1
                    self.hist[12] += 1
                if input[i-7] == input[i-6] == input[i-5] == input[i-4] == input[i-3] == input[i-2] == input[i-1] == input[i] == 1:
                    stat[13] += 1
                    self.hist[13] += 1
            if i >= 8:
                if input[i-8] == input[i-7] == input[i-6] == input[i-5] == input[i-4] == input[i-3] == input[i-2] == input[i-1] == input[i] == 0:
                    stat[14] += 1
                    self.hist[14] += 1
                if input[i-8] == input[i-7] == input[i-6] == input[i-5] == input[i-4] == input[i-3] == input[i-2] == input[i-1] == input[i] == 1:
                    stat[15] += 1
                    self.hist[15] += 1
            if i >= 9:
                if input[i-9] == input[i-8] == input[i-7] == input[i-6] == input[i-5] == input[i-4] == input[i-3] == input[i-2] == input[i-1] == input[i] == 0:
                    stat[16] += 1
                    self.hist[16] += 1
                if input[i-9] == input[i-8] == input[i-7] == input[i-6] == input[i-5] == input[i-4] == input[i-3] == input[i-2] == input[i-1] == input[i] == 1:
                    stat[17] += 1
                    self.hist[17] += 1
 

        inputF.close()
       
        suma = 0
        for i in range(0, len(stat)):
            suma += stat[i]

        chi = []

        for i in range(0, len(stat)):
            chi.append(pow((stat[i]-suma*self.p_i[i]),2)/(suma*self.p_i[i]))

        chi_suma = 0

        for i in range(0, len(chi)):
            chi_suma +=chi[i]

        statF = open('stat\stat_'+plik, 'a')

        statF.write('%s %f\n' % (key, chi_suma))
        statF.write('%f\n' % chi_suma)
        for i in range(0, len(self.index)):
            statF.write('%s %d\n' % (self.index[i], stat[i]))

        statF.close()

    def print_hist(self,value, plik):
        statF = open('stat\stat_'+plik, 'a')
        statF.write('\n wyniki uśrednione: \n')
        for i in range(0, len(self.hist)):
            statF.write('%s %d\n' % (self.index[i], (self.hist[i])/value))


        suma = 0
        tab = []
        for i in range(0, len(self.hist)):
            tab.append(int(self.hist[i]/value))
            suma += tab[i]

        chi = []

        for i in range(0, len(tab)):
            chi.append(pow((tab[i]-suma*self.p_i[i]), 2)/(suma*self.p_i[i]))
            

        chi_suma = 0

        for i in range(0, len(chi)):
            
            chi_suma +=chi[i]
        
        statF.write('sredni wynik testu chi kwadrat = %f\n' % chi_suma)
        statF.close()

    def stat_wykres(self, name):
        stat = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        st = []
        # stat[0] -> 00
        # stat[1] -> 11
        # stat[2] -> 000
        # stat[3] -> 111
        # stat[4] -> 0000
        # stat[5] -> 1111
        # stat[6] -> 00000
        # stat[7] -> 11111
        # stat[8] -> 000000
        # stat[9] -> 111111
        if name == 'input':
            inputF = open(name+'.txt', 'r')
        else:
            inputF = open('output'+name+'.txt', 'r')
        input = list(map(int, map(str.strip, inputF.readlines())))

        for i in range(0, len(input)):
            if i >= 1:
                if input[i-1] == input[i] == 0:
                    stat[0] += 1
                if input[i-1] == input[i] == 1:
                    stat[1] += 1
            if i >= 2:
                if input[i-2] == input[i-1] == input[i] == 0:
                    stat[2] += 1
                if input[i-2] == input[i-1] == input[i] == 1:
                    stat[3] += 1
            if i >= 3:
                if input[i-3] == input[i-2] == input[i-1] == input[i] == 0:
                    stat[4] += 1
                if input[i-3] == input[i-2] == input[i-1] == input[i] == 1:
                    stat[5] += 1
            if i >= 4:
                if input[i-4] == input[i-3] == input[i-2] == input[i-1] == input[i] == 0:
                    stat[6] += 1
                if input[i-4] == input[i-3] == input[i-2] == input[i-1] == input[i] == 1:
                    stat[7] += 1
            if i >= 5:
                if input[i-5] == input[i-4] == input[i-3] == input[i-2] == input[i-1] == input[i] == 0:
                    stat[8] += 1
                if input[i-5] == input[i-4] == input[i-3] == input[i-2] == input[i-1] == input[i] == 1:
                    stat[9] += 1
            if i >= 6:
                if input[i-6] == input[i-5] == input[i-4] == input[i-3] == input[i-2] == input[i-1] == input[i] == 0:
                    stat[10] += 1
                if input[i-6] == input[i-5] == input[i-4] == input[i-3] == input[i-2] == input[i-1] == input[i] == 1:
                    stat[11] += 1
            if i >= 7:
                if input[i-7] == input[i-6] == input[i-5] == input[i-4] == input[i-3] == input[i-2] == input[i-1] == input[i] == 0:
                    stat[12] += 1
                if input[i-7] == input[i-6] == input[i-5] == input[i-4] == input[i-3] == input[i-2] == input[i-1] == input[i] == 1:
                    stat[13] += 1
            if i >= 8:
                if input[i-8] == input[i-7] == input[i-6] == input[i-5] == input[i-4] == input[i-3] == input[i-2] == input[i-1] == input[i] == 0:
                    stat[14] += 1
                if input[i-8] == input[i-7] == input[i-6] == input[i-5] == input[i-4] == input[i-3] == input[i-2] == input[i-1] == input[i] == 1:
                    stat[15] += 1
            if i >= 9:
                if input[i-9] == input[i-8] == input[i-7] == input[i-6] == input[i-5] == input[i-4] == input[i-3] == input[i-2] == input[i-1] == input[i] == 0:
                    stat[16] += 1
                if input[i-9] == input[i-8] == input[i-7] == input[i-6] == input[i-5] == input[i-4] == input[i-3] == input[i-2] == input[i-1] == input[i] == 1:
                    stat[17] += 1
        
        plt.figure(1)
        plt.bar(self.index, stat, align = 'center')
        if name == 'input':
            plt.title('Histogram dla %s' % name)
        else:
            plt.title('Histogram dla scramblera %s' % name)
        plt.ylabel('ilość wystąpień')
        plt.grid()
        plt.xticks(rotation = 90)
        
    #    plt.close(1)

        inputF.close()

    def count(self, name):
        stat = []
        if name == 'input':
            inputF = open(name+'.txt', 'r')
        else:
            inputF = open('output'+name+'.txt', 'r')
        input = list(map(int, map(str.strip, inputF.readlines())))
        
        h = []
        tab = []
        for i in range(0, 256):
            h.append(i)
            stat.append(0)
        
        
        for i in range(0, len(input)):
            if i % 7 == 0:
                stat[konw(tab)] += 1
                tab = []
                tab.append(input[i])
            tab.append(input[i])
        
        h = []
        for i in range(0, 256):
            h.append(i)
        plt.figure(2)
        plt.bar(h, stat, align = 'center')
        plt.grid()
        plt.xlabel('wartości ósemek bitów')
        plt.ylabel('ilość wystąpień')
        plt.title('Histogram ósemek bitów dla %s' % name)



def konw(tab):
    v = [128, 64, 32, 16, 8, 4, 2, 1]
    k = 0
    for i in range(0, len(tab)):
        k += v[i] * tab[i]
    return k