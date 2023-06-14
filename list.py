#more about indexing:
"""a=[12,20,34,'phitron']
print(a[0])
print(a [-3])
print(a[-1])
print(len(a))
a[-3]=500
print(a)
if 20 in a:
    print('found')
else:
    print('no found')
for i in range(len(a)):
        print(a[i])
for i in range(-1,len(a)-1,-1):
     print (a[i])
"""
#list slicing:
"""a=[12,13,4,'phitrin','Mango',[12.5,10]]

print(a[::])
print(a[1::])
print(a[2::2])
print(a[::-1])
 """
'''a=[1,2,3]
b=[4,5,6]
c=a+b
print(c)'''
'''a=[1,2,3,4,5]
a.insert(2,100)
print(a)'''
'''a=[1,2,3,4,5]
b=a.copy()
print(b)'''
#a=[1,2,3,2,3,2,3,2,2,4,2,5,2]
#print(a.count(2))
'''a=[12,2,5,6]
a.extend.[23,3,34,]
print(a)
'''
#full list ar element delete kora:
'''a=[2,2,3,4,5]
a.clear()
print(a)'''
#shot
#a=[1,3,4,3,2,5,1,7]
#a.sort(reverse=True)
#print(a)
#a.sort(reverse=False)
#print(a)
'''a=[10,20,30,40,50]
b =[i+5 for i in a]
print(b)'''
'''a= 'hello World'
b= [i for i in a]
print(b)'''
'''a =[ i for i in range(1,20,2)]
print(a)
a=list(range(2,20,2))
print(a)'''
'''a=[]
for i in range(1,20):
    if i%3 ==0:
        a.append(i)
    print(a)
'''
#b =[i for i in range(1,20) if i%3==0 or i%5==0]
#print(b)
'''a =[]
for i in range(20):
    if i%2==0:
        a.append('even')
    if i%2==1:
       a.append("odd")
print(a)'''
#b =['even' if i%2==0 else 'odd' for i in range(20)]
#print(b)
#2d list comprehesoin
matrix= [[1,2],[3,4],[5,6],[7,8]]

#transpose maxtrix

'''a =[]
for row in range(2):
    b=[]
    for col in matrix:
        b.append(col[row])
    a.append(b)
print(a)'''
 
        