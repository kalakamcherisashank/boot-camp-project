#import hash library
import hashlib
string = input("enter string: ")
encoded=string.encode()
#using SHA224 algorithm from hashlib
hash_object = hashlib.sha224(encoded)
hex_dig = hash_object.hexdigest()
print(hex_dig)