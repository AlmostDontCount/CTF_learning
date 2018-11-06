#python2
#produce XOR combination of two equal buffers

def XOR(x1,x2):
    s = ''
    for i in range(len(x1)):
        s += chr(ord(x1[i])^ord(x2[i]))
    string = s.encode('hex')
    return string

s1='1c0111001f010100061a024b53535009181c'

s2 = '686974207468652062756c6c277320657965'

s1_decoded = s1.decode('hex')

s2_decoded =s2.decode('hex')

length = len(s1_decoded)

res1 = XOR(s1_decoded,s2_decoded)

from binascii import unhexlify, b2a_base64

s1_decoded = unhexlify(s1)

s2_decoded = unhexlify(s2)

res2 = XOR(s1_decoded,s2_decoded)

print res1

print res2
