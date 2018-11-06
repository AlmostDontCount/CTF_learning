#python3 solutions for cryptopals challeng set1-1
#convert hex to base64
import codecs
code = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
b64 = codecs.encode(codecs.decode(code, 'hex'), 'base64').decode()
print (b64)
