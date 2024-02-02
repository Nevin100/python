#tuple data structrue and illustrations of various operations.. 

#accesing an element of a tuple with the help of index number
tple1=(1,2,3,4,5,6,"ok",4.6)
print(tple1[0])
print(tple1[-3])

#illustration of a nested tuple 
tple2=(1,2,3,4,5,6,(4,6,8,5),4.6)
print(tple2[6][2])
 
#concatenation of tuple
tple3= tple2 + tple1
print(tple3) 

#Repetition of tuple with *
tple4= tple1 * 3
print(tple4)
 
#checking whether an element exist in tuple
print(1 in tple1)

#iteration of a tuple
for i in tple1:
     print(i)
      
#tuple is immutable so we can change an element of typle with index accessing... 