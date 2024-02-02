#Various sets methods and functions with illustrations..
'''
add
clear
copy
discard
issubset
issuperset
pop
remove
'''

#1.)To add an element to a set
st1={1,2,3,4,5,6}
st1.add(7)
print(st1)

#2.)To clear out the set..
st2={1,2,3,4,5,6}
st2.clear()
print(st2)

#3.)To copy a set to a new identifier..
st3=st1.copy()
print(st3)

#4.)To discard an element of the set..
st4={1,2,3,4,5,6}
st4.discard(3)
print(st4)

#5.)Similiar to discard but if suppose an element which is not presesnt in the set is being removed by remove... error occurs but with discard no error occurs...  
st5={1,2,3,4,5,6}
st5.remove(2)
print(st5)

#6.)For determining whether a is subset of b?????& b is superset of a????
a={1,2,3}
b={1,2,3,4,5,6,7,8}
print(a.issubset(b))
print(a.issuperset(b))

#7.)To remove the last itme of an element...
st6={1,2,3,4,5,6}
st6.pop()
print(st6)





