'''
Append
Reverse
pop
copy
remove and clr
index
insert
max and min
count and length 
'''
#1.) Appending an element in list...
lst=[1,2,3,4,5,6,7,8,9,0]
lst.append(10)
print(lst)

#2.)removing an element in the list....
lst1=[1,2,3,4,5,6,7,8,9,0]
lst1.remove(5)
print(lst1)

#3.clearing all the elements in the list...
lst2=[1,2,3,4,5,6,7,8,9,0]
lst2.clear()
print(lst2)

#4.)copying a list to a new identifier...
lst3=[1,2,3,4,5,6,7,8,9,0]
lst_3=lst3.copy()
print(lst_3)

#5.)determination of an index of an element..
lst4=[1,2,3,4,5,6,7,8,9,0] 
i = lst4.index(6)
print(i)

#6.)To pop out an element of a list of a particular index...
lst6=[1,2,3,4,5,6,7,8,9,0]
lst6.pop(6)
print(lst6)

#7.)To show the maximum value in a given list...
lst7=[1,2,3,4,5,6,7,8,9,0]
print(max(lst7))

#8.)To show the ,minimum value in a given list...
lst8=[1,2,3,4,5,6,7,8,9,0]
print(min(lst8))

#9.)To reverse a list
lst9=[1,2,3,4,5,6,7,8,9,0]
lst_9=lst9.reverse()
print(lst_9)

#10.)To determine the length of a list..
lst10=[1,2,3,4,5,6,7,8,9,0]
a=len(lst10)
print(a)

