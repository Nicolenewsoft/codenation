import hashlib
str = "yv rikju vfisu tfui efj ifclu ofki gifrcudi jxue ofk qiu efj kiyew uefkwx. kebefme"
  
# encoding GeeksforGeeks using encode() 
# then sending to SHA1() 
result = hashlib.sha1(str.encode()) 
  
# printing the equivalent hexadecimal value. 
#print("The hexadecimal equivalent of SHA1 is : ") 
print(result.hexdigest())