#import hash library
import hashlib
string = input("enter string: ")
encoded=string.encode()
#using SHA256 algorithm from hash library
hash_object = hashlib.sha256(encoded)
hex_dig = hash_object.hexdigest()
print(hex_dig)