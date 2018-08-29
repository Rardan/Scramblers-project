from generatory import *
from scramblery import *
from statystyka import *
def test():
    st1 = Statystyka()
    st2 = Statystyka()
    st3 = Statystyka()
    st4 = Statystyka()
    st5 = Statystyka()
    st6 = Statystyka()
    gen = Generator()
    v34 = V34()
    dvb = DVB()
    x43 = X43()
    x7x6 = X7X6()
    x16 = X16()
    x24x22 = X24X22()
#    gen.generate(100000)

    inputF = open('input.txt', 'w')

    for i in range (0, 100000):
        inputF.write('%d\n' % 0)

    inputF.close()   

    for j in range (0, 100):
        
    
        key = []
        key = gen.generate_key(23)
        key2 = []
        key_stat = []
        for i in range(len(key)):
            key2.append(key[i])
            key_stat.append(key[i])

    
        v34.scrambler('input.txt','outputV34.txt',key)
        st1.stat('outputV34.txt', key_stat)
        v34.descrambler('outputV34.txt','outputV34_de.txt',key2)

    for j in range (0, 100):
        
        keyy = []
        keyy = gen.generate_key(15)
        keyy2 = []
        keyy_stat = []
        for i in range(len(keyy)):
            keyy2.append(keyy[i])
            keyy_stat.append(keyy[i])
    
        
        dvb.scrambler('input.txt', 'outputDVB.txt', keyy)
        st2.stat('outputDVB.txt', keyy_stat)
        dvb.descrambler('outputDVB.txt', 'outputDVB_de.txt', keyy2)

    for j in range (0, 100):
        
        key43 = []
        key43 = gen.generate_key(43)
        key43_1 = []
        key43_2 = []
        for i in range(len(key43)):
            key43_1.append(key43[i])
            key43_2.append(key43[i])
    
        
        x43.scrambler('input.txt', 'outputx43.txt', key43)
        st3.stat('outputx43.txt', key43_2)
        x43.descrambler('outputx43.txt', 'outputx43_de.txt', key43_1)

    for j in range (0, 100):
        
        key7 = []
        key7 = gen.generate_key(7)
        key7_1 = []
        key7_2 = []
        for i in range(len(key7)):
            key7_1.append(key7[i])
            key7_2.append(key7[i])
    
        
        x7x6.scrambler('input.txt', 'outputx7x6.txt', key7)
        st4.stat('outputx7x6.txt', key7_2)
        x7x6.descrambler('outputx7x6.txt', 'outputx7x6_de.txt', key7_1)


    for j in range (0, 100):
        key = []
        key = gen.generate_key(16)
        key_1 = []
        key_2 = []
        for i in range(0, len(key)):
            key_1.append(key[i])
            key_2.append(key[i])
        x16.scrambler('input.txt', 'outputx16.txt', key)
        st5.stat('outputx16.txt', key_2)
        x16.descrambler('outputx16.txt', 'outputx16_de.txt', key_1)


    for j in range (0, 100):
        keyy = []
        keyy = gen.generate_key(24)
        keyy_1 = []
        keyy_2 = []
        for i in range(0, len(keyy)):
            keyy_1.append(keyy[i])
            keyy_2.append(keyy[i])

        x24x22.scrambler('input.txt', 'outputx24x22.txt', keyy)
        st6.stat('outputx24x22.txt', keyy_2)
        x24x22.descrambler('outputx24x22.txt', 'outputx24x22_de.txt', keyy_1)

 #   st1.print_hist(100, 'outputV34')
 #   st2.print_hist(100, 'outputDVB')
 #   st3.print_hist(100, 'outputx43')
 #   st4.print_hist(100, 'outputx7x6')
 #   st5.print_hist(100, 'outputx16.txt')
 #   st6.print_hist(100, 'outputx24x22.txt')

def test2():
    inputF = open('input.txt', 'w')
    for i in range (0, 100000):
        inputF.write('%d\n' % 0)
    inputF.close()

    dvb = DVB()
    v34 = V34()
    x43 = X43()
    x7x6 = X7X6()
    x16 = X16()
    x24x22 = X24X22()
    key1 = [0,0,0,0]
    key2 = [0,0,0,0]
    key3 = [0,0,0,0]
    key4 = [0,0,0,0]
    key5 = [0,0,0,0]
    key6 = [0,0,0,0]
    key1[0] = [0,1,0,0,0,1,1,1,0,0,1,1,1,1,0] #dvb
    key1[1] = [0,1,0,1,0,1,0,1,0,0,1,1,0,0,1]
    key1[2] = [0,1,0,0,1,0,0,1,1,0,1,0,1,0,1]
    key1[3] = [0,1,1,1,1,1,1,1,0,0,0,1,1,1,0]
    key2[0] = [0,0,0,1,1,0,0,1,1,1,1,0,1,1,1,0,0,0,1,1,0,1,1] #v.34
    key2[1] = [1,1,0,1,1,0,1,1,0,0,0,1,0,1,0,1,0,1,1,1,0,1,1]
    key2[2] = [1,1,0,0,0,1,1,1,1,1,0,1,1,0,1,1,1,0,1,0,0,0,0]
    key2[3] = [0,1,0,1,1,0,0,1,1,0,0,0,1,0,0,1,1,1,1,0,1,0,0]
    key3[0] = [0,1,1,0,0,1,0] #x7x6
    key3[1] = [1,0,1,1,0,1,1]
    key3[2] = [1,1,1,1,1,1,0]
    key3[3] = [1,1,1,1,1,0,1]
    key4[0] = [1,0,1,1,0,0,0,1,1,0,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,1,0,1,1,1,0,1,0] #x43
    key4[1] = [1,0,1,0,0,0,0,1,0,1,1,1,1,1,1,1,1,0,1,0,1,0,0,0,1,0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,1,0,0]
    key4[2] = [0,0,1,1,1,1,1,0,0,0,1,0,1,0,0,1,0,0,0,0,0,1,1,0,1,1,0,0,0,1,1,0,0,1,0,0,1,1,1,0,1,1,1]
    key4[3] = [1,1,1,1,1,1,0,1,1,0,0,1,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,1,1,1,1,0,0,1,0,0,1,1,1,0,1,0]
    key5[0] = [0,0,0,0,0,0,0,0,1,0,1,1,1,1,1,1,1,0,0,1,0,0,0,1] #x24x22
    key5[1] = [1,0,1,1,1,1,0,0,0,0,1,1,0,0,0,1,0,1,1,1,0,0,1,0]
    key5[2] = [0,1,0,0,0,1,1,1,0,1,0,0,1,1,0,0,1,1,1,0,1,0,1,1]
    key5[3] = [1,0,1,1,0,0,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,1,0,0]
    key6[0] = [0,0,1,1,0,0,1,1,1,1,0,1,0,1,0,0] #x16
    key6[1] = [0,0,0,0,1,0,1,0,1,1,1,1,0,0,1,1]
    key6[2] = [1,1,1,1,1,0,0,1,0,1,0,1,1,1,1,1]
    key6[3] = [0,0,0,0,0,1,0,0,1,1,0,0,0,0,0,0]
    
    st = Statystyka()
#    for i in range(0, 24):
#        st.append(Statystyka())

    key1_1 = [0,0,0,0]
    key2_1 = [0,0,0,0]
    key3_1 = [0,0,0,0]
    key4_1 = [0,0,0,0]
    key5_1 = [0,0,0,0]
    key6_1 = [0,0,0,0]

    for i in range(0, 4):
        for j in range(0, len(key1)):
            key1_1[i] = key1[i]
#    print(key1)
#    print(key1_1)
    for i in range(0, 4):
        for j in range(0, len(key1)):
            key2_1[i] = key2[i]
    for i in range(0, 4):
        for j in range(0, len(key2)):
            key3_1[i] = key3[i]
    for i in range(0, 4):
        for j in range(0, len(key3)):
            key3_1[i] = key3[i]
    for i in range(0, 4):
        for j in range(0, len(key4)):
            key4_1[i] = key4[i]
    for i in range(0, 4):
        for j in range(0, len(key5)):
            key5_1[i] = key5[i]
    for i in range(0, 4):
        for j in range(0, len(key6)):
            key6_1[i] = key6[i]

    for i in range(0, 4):
        dvb.scrambler('input.txt', 'outputDVB.txt', key1[i])
        st.stat('outputDVB.txt', key1_1[i])
       
        v34.scrambler('input.txt', 'outputv34.txt', key2[i])
        st.stat('outputv34.txt', key2_1[i])
        
        x7x6.scrambler('input.txt', 'outputx7x6.txt', key3[i])
        st.stat('outputx7x6.txt', key3_1[i])
        
        x43.scrambler('input.txt', 'outputx43.txt', key4[i])
        st.stat('outputx43.txt', key4_1[i])
        
        x24x22.scrambler('input.txt', 'outputx24x22.txt', key5[i])
        st.stat('outputx24x22.txt', key5_1[i])
        
        x16.scrambler('input.txt', 'outputx16.txt', key6[i])
        st.stat('outputx16.txt', key6_1[i])