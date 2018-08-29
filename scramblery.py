def xor(a, b):
    if a != b:
        return 1
    else:
        return 0

class DVB():
#	klucz = []
#	key = []
#	def __init__ (self, key):
#		self.key = key

	def scrambler(self,plik_in, plik_out, key):
#		klucz = []
		klucz = key
		inputF = open(plik_in, 'r')
		outputF = open(plik_out, 'w')

		input = list(map(int, map(str.strip, inputF.readlines())))


		output = []


		for i in range(0, len(input)):
			x = xor(klucz[13], klucz[14])
			klucz.pop()
			klucz.insert(0, x)
			output.append(xor(x, input[i]))      

		outputF.write("\n".join(str(x) for x in output))

		inputF.close()
		outputF.close()


	def descrambler(self,plik_in, plik_out, key):
#		klucz = []
		klucz = key
		inputF = open(plik_in, 'r')
		outputF = open(plik_out, 'w')

		input = list(map(int, map(str.strip, inputF.readlines())))

		output = []

		for i in range(0,len(input)):
			x = xor(klucz[13], klucz[14])
			klucz.pop()
			klucz.insert(0, x)
			output.append(xor(x, input[i]))

		outputF.write("\n".join(str(x) for x in output))

		inputF.close()
		outputF.close()




class V34():
#	klucz = []
#	key = []
#	def __init__(self, key):
#		self.key = key

	def scrambler(self,plik_in, plik_out, key):
	#	klucz = []
		klucz = key
		inputF = open(plik_in, 'r')
		outputF = open(plik_out, 'w')

		input = list(map(int, map(str.strip, inputF.readlines())))

		output = []


		for i in range(0, len(input)):
			x = xor(klucz[17], klucz[22])
			klucz.pop()
			klucz.insert(0, xor(x, input[i]))
			output.append(xor(x, input[i]))


		outputF.write("\n".join(str(x) for x in output))

		inputF.close()
		outputF.close()

	def descrambler(self,plik_in, plik_out, key):
	#	klucz = []
		klucz = key
		inputF = open(plik_in, 'r')
		outputF = open(plik_out, 'w')

		input = list(map(int, map(str.strip, inputF.readlines())))


		output = []

		for i in range(0,len(input)):
			x = xor(klucz[17], klucz[22])
			klucz.pop()
			klucz.insert(0, input[i])
			output.append(xor(x, input[i]))

		outputF.write("\n".join(str(x) for x in output))

		inputF.close()
		outputF.close()


class X43():
	def scrambler(self,plik_in, plik_out, key):
		klucz = key
		inputF = open(plik_in, 'r')
		outputF = open(plik_out, 'w')

		input = list(map(int, map(str.strip, inputF.readlines())))

		output = []

		for i in range(0, len(input)):
			x = xor(klucz[42], input[i])
			klucz.pop()
			klucz.insert(0, x)
			output.append(x)
            
		outputF.write("\n".join(str(x) for x in output))
		inputF.close()
		outputF.close()

	def descrambler(self,plik_in, plik_out, key):
		klucz = key
		inputF = open(plik_in, 'r')
		outputF = open(plik_out, 'w')

		input = list(map(int, map(str.strip, inputF.readlines())))

		output = []

		for i in range (0, len(input)):
			x = xor(klucz[42], input[i])
			klucz.pop()
			klucz.insert(0, input[i])
			output.append(x)

		outputF.write('\n'.join(str(x) for x in output))
		inputF.close()
		outputF.close()

class X7X6():
	def scrambler(self,plik_in, plik_out, key):
		klucz = key
		inputF = open(plik_in, 'r')
		outputF = open(plik_out, 'w')

		input = list(map(int, map(str.strip, inputF.readlines())))
		output = []

		for i in range(0, len(input)):
			x = xor(klucz[5], klucz[6])
			klucz.pop()
			klucz.insert(0, x)
			output.append(xor(x, input[i]))

		outputF.write('\n'.join(str(x) for x in output))
		inputF.close()
		outputF.close()

	def descrambler(self,plik_in, plik_out, key):
		klucz = key
		inputF = open(plik_in, 'r')
		outputF = open(plik_out, 'w')

		input = list(map(int, map(str.strip, inputF.readlines())))
		output = []

		for i in range(0, len(input)):
			x = xor(klucz[5], klucz[6])
			klucz.pop()
			klucz.insert(0, x)
			output.append(xor(x, input[i]))

		outputF.write('\n'.join(str(x) for x in output))
		inputF.close()
		outputF.close()

		# +sync
	def scrambler_sync(self,plik_in, plik_out, key):
		klucz = key
		inputF = open(plik_in, 'r')
		outputF = open(plik_out, 'w')

		input = list(map(int, map(str.strip, inputF.readlines())))
		output = []

		for i in range(0, len(input)):
			if i % 7 == 0:
				klucz = []
				klucz = key
			x = xor(klucz[5], klucz[6])
			klucz.pop()
			klucz.insert(0, x)
			output.append(xor(x, input[i]))

		outputF.write('\n'.join(str(x) for x in output))
		inputF.close()
		outputF.close()

	def descrambler_sync(self,plik_in, plik_out, key):
		klucz = key
		inputF = open(plik_in, 'r')
		outputF = open(plik_out, 'w')

		input = list(map(int, map(str.strip, inputF.readlines())))
		output = []

		for i in range(0, len(input)):
			if i % 7 == 0:
				klucz = []
				klucz = key
			x = xor(klucz[5], klucz[6])
			klucz.pop()
			klucz.insert(0, x)
			output.append(xor(x, input[i]))

		outputF.write('\n'.join(str(x) for x in output))
		inputF.close()
		outputF.close()

class X24X22():
	def scrambler(self,plik_in, plik_out, key):
		klucz = key
		inputF = open(plik_in, 'r')
		outputF = open(plik_out, 'w')

		input = list(map(int, map(str.strip, inputF.readlines())))

		output = []


		for i in range(0, len(input)):
			x = xor(klucz[21], klucz[23])
			klucz.pop()
			klucz.insert(0, xor(x, input[i]))
			output.append(xor(x, input[i]))


		outputF.write("\n".join(str(x) for x in output))

		inputF.close()
		outputF.close()

	def descrambler(self,plik_in, plik_out, key):
		klucz = key
		inputF = open(plik_in, 'r')
		outputF = open(plik_out, 'w')

		input = list(map(int, map(str.strip, inputF.readlines())))


		output = []

		for i in range(0,len(input)):
			x = xor(klucz[21], klucz[23])
			klucz.pop()
			klucz.insert(0, input[i])
			output.append(xor(x, input[i]))

		outputF.write("\n".join(str(x) for x in output))

		inputF.close()
		outputF.close()

class X16():
	def scrambler(self,plik_in, plik_out, key):
		klucz = key
		inputF = open(plik_in, 'r')
		outputF = open(plik_out, 'w')

		input = list(map(int, map(str.strip, inputF.readlines())))
		output = []

		for i in range(0, len(input)):
			x = klucz[15]
			klucz.pop()
			klucz.insert(0, x)
			output.append(xor(x, input[i]))

		outputF.write('\n'.join(str(x) for x in output))
		inputF.close()
		outputF.close()

	def descrambler(self,plik_in, plik_out, key):
		klucz = key
		inputF = open(plik_in, 'r')
		outputF = open(plik_out, 'w')

		input = list(map(int, map(str.strip, inputF.readlines())))
		output = []

		for i in range(0, len(input)):
			x = klucz[15]
			klucz.pop()
			klucz.insert(0, x)
			output.append(xor(x, input[i]))

		outputF.write('\n'.join(str(x) for x in output))
		inputF.close()
		outputF.close()