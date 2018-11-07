import binascii
from Crypto.Util.strxor import strxor

encodedS = '1c0111001f010100061a024b53535009181c'
encodedT = '686974207468652062756c6c277320657965'
encodedExpectedU = '746865206b696420646f6e277420706c6179'

s = binascii.unhexlify(encodedS)
t = binascii.unhexlify(encodedT)
expectedU = binascii.unhexlify(encodedExpectedU)

u = strxor(s, t)
print(u)
print(expectedU)
def XOR(x1,x2):
	x = ''
	for i in range(len(x1)):
		x += chr(x1[i]^x2[i])
	return x

x = XOR(s,t)

import codecs

res = codecs.encode(u,'hex')

print (x)
print (res)