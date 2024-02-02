#list data structure and various fundamental operations

#1.)List's element accessingby by index
lst=[1,2,3,4,5,"abcdef"] 
print(lst[0])

#2.)nested list illustration
lst1=[1,2,3,4,5,6,7,[1,2,3]]
print(lst1[-1][1])

#3.)joining of the list
lst3=lst1+lst 
print(lst3)

#4.)repititon of list by *
lst4= lst3 * 5
print(lst4)

#5.)iteration 
for i in lst3:
    print(i)
    
#6.)checking of an element in a list
print(10 in lst)    