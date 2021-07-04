#import hashlibrary
import hashlib 
string = input("enter string: ")
encoded=string.encode()
#md5 
result = hashlib.md5(encoded)
print("String : ", end ="")
print(string)
print("Hash Value : ", end ="")
print(result)
print("Hexadecimal equivalent: ",result.hexdigest())