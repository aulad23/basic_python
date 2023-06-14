#function in python:
'''
funtion ki?
particul kaj korba
bar bar bebohar kora jaba
input niba seta output hisaba bebhohar korba

1| builted function:ata python ja function build aca seita
2|user defind function:user nija cretive kora bebhhor korba!

'''
'''
1.define a function:
2. function calling:
'''
#def greeting ():#define a function:
    #print('hello Good morning')

#greeting()#calling a function:


#arguments vs parameters in function:
#def sum(a,b): 
    #sum ai betor a,b ata holo parameters
    #print(f'the sumation of {a} and {b}={a+b}')

#sum(2,3)#2,3 ata holo arguments 


#defult parameters and keyword argumerts:

'''def greetings(name='aulad',age='23'):
    print(f'hello {name}.you ar {age } years odd')

greetings('jiku ahemad',30)'''

#print vs return in function:
'''
1|print mani holo fixid rakla kaj tahola print
2|return mani fixed na maja kicu kaj korla lagba
     
'''
def sum(a,b): 
    print(a+b)
sum(2,4)

def sum_with_return(a,b):
    return a+b

result=sum_with_return(2,3)
result += 4
print(sum_with_return)
