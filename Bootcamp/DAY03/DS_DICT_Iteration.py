#Iteration of the elements of dictionary...

d={1:"red",2:"black",3:"grey",4:"yellow",5:"blue"}
#1.)iterating key and items with for loop...
for k,v in d.items():
    print(k,":",v)
    
#2.)iterating only keys of a given dictionary with for loop
for keys in d.keys():
    print("The keys of the given dictionary are:",keys)
    
#3.)iterating only values of a given dictionary with for loop
for values in d.values():
    print("The values of the given dictionary are:",values)
    
