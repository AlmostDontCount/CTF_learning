#python2 solution for cryptopals challenge set1-1
#convert hex to base64

from binascii import unhexlify, b2a_base64

string = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'

result = b2a_base64(unhexlify(string))

#the trick is we use unhexlify to convert hex  string into bytes

#then we use b2a_base64 to convert bytes into base64

print result

print'\n'

print unhexlify(string)

#or we can do it like

print string.decode('hex').encode('base64')

print string.decode('hex')

