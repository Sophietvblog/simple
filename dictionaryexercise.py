movie1={"director":"steven", "name":"shark","country":"US", "show":"yes"}
print (movie1)
print ('director' in movie1)
print (len(movie1))
print (movie1.keys())
print (movie1.values())
try:
    movie1['censored':'yes']
except:
    print (movie1)
del movie1['director']
print (movie1)
temp=movie1.pop("name")
print (movie1)
print (temp)