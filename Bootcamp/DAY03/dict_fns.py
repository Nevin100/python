#dictionary functions with illustrations..
"""
vlear
copy
get
items
keys
values
pop
popitem
update
"""

#1.)To clear a dictionary... results empty dicionary..
d={1:"red",2:"black",3:"grey",4:"yellow",5:"blue"}
d.clear()
print(d)

#2.)To copy a dictionary into a new identifier..
d={1:"red",2:"black",3:"grey",4:"yellow",5:"blue"}
d1=d.copy()
print(d1)

#3.)To determine the value of a given key...
d2={1:"red",2:"black",3:"grey",4:"yellow",5:"blue"}
print(d2.get(2))
#if no such key exist.. you can set the default value too..
print(d2.get(8,"green"))

#4.)To fetch all the items in list format...
d3={1:"red",2:"black",3:"grey",4:"yellow",5:"blue"}
print(d3.items)

#4.)To fetch all the keys of a dictionary...
d4={1:"red",2:"black",3:"grey",4:"yellow",5:"blue"}
print(d4.keys())

#5.)To fetch all the values of a dictionary...
d5={1:"red",2:"black",3:"grey",4:"yellow",5:"blue"}
print(d5.values())

#6.)To remove a specific item from a dictionary...
d6={1:"red",2:"black",3:"grey",4:"yellow",5:"blue"}
d6.pop(1)
print(d6)

#7.)To remove the last item from a dictionary...
d7={1:"red",2:"black",3:"grey",4:"yellow",5:"blue"}
d7.popitem()

#8.)To update a dictionary...
d8={1:"red",2:"black",3:"grey",4:"yellow",5:"blue"}
d8.update({3:"brown",6:"sapphire"})
print(d8)
 








