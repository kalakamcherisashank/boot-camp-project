import hashlib
string = input("enter string: ")
encoded=string.encode()
hash_object = hashlib.sha1(encoded)
hex_dig = hash_object.hexdigest()
print(hex_dig)
