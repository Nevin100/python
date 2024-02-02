#Sets structure and various fundamental operations and concepts..

#1.)printing a set...
st={1,2,3,4,5,6}
print(st)

#2.)Union of two sets..
st1={1,2,3,4,5,6}
st2={7,8,9,0}
st3=st2.union(st1)
print(st3)

#3.)Intersection of two sets..
st4={1,2,3,4,5,6}
st5={7,8,9,0}
st6=st4.intersection(st5)
print(st6)

#4.)Difference between two sets..
st7={1,2,3,4,5,6}
st8={7,8,9,0}
st9=st7.difference(st8)
print(st9)

#5.)Symmetric difference of two sets..
st10={1,2,3,4,5,6}
st11={7,8,9,0}
st12=st10.symmetric_difference(st11)
print(st12)

#6.)traversing each element of the set..
st13={1,2,3,4,5,6}
for i in st13:
    print(i)
    
    