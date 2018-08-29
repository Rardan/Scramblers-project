import random

def xor(a, b):
    if a != b:
        return 1
    else:
        return 0

class Generator:

	def generate(self, x):
		inputF = open('input.txt', 'w')

		tab = []

		for i in range (0, x):
			r = random.randint(0, 1)
			tab.append(r)
			inputF.write('%d\n' % r)

		inputF.close()

	def generate_key(self, x):
		tab = []

		for i in range (0, x):
			r = random.randint(0, 1)
			tab.append(r)

		return tab

	def generate_crc(self, x):
		tab = []
		r = 1
		tab.append(r)
		for i in range (1, x):
			r = random.randint(0, 1)
			tab.append(r)

		return tab


class Generator_ramek:

	def generate(self, crc):
		inputF = open('ramka.txt', 'w')

		for i in range(1):

			tab = []
			tab2 = []
			for j in range(7):
				tab.append(1)
			

			for j in range(54):
				r = random.randint(0,1)
				tab.append(r)

			for j in range(32):
				tab.append(0)
			
			for j in range(86):
				tab2.append(0)
			
			for j in range(86):
				tab2[j] = tab[j+7]
			
			for j in range(54):
				if tab2[j] != 0:
					for k in range(33):
						tab2[j+k] = xor(tab2[j+k], crc[k])

			for j in range(32):
				tab[j+7+54] = tab2[j+54]

			inputF.write("\n".join(str(x) for x in tab))
			inputF.write("\n")

		inputF.close()

