'''
lecture 8
'''

#key word arguments
'''
def my_function(a,b):
    result = a + b
    return result
    
print(my_function(1,2))
'''

'''
def my_function(a,b):
    result = a + b
    
    print(a)
    print(b)
    
    return result
    
print(my_function(b=1, a=2))
'''

#The void statement/function
def my_function(a,b=0):
    result = a + b
    
    print(a)
    print(b)
    
    #return result
    
print(my_function(1))


#Absolute value exercise
'''
def cal_abs(a):
    if a > 0:
        return a
    if a < 0:
        return -a
        
print(cal_abs(1))
'''

#Exercise 1
def cal_abs(a):
    if type(a) is str:
        return "wrong data type"
    elif a >= 0:
        return a
    else:
        return -a
        
print(cal_abs(1))

#Exercise 2
def cal_sigma(n,m):

    result = 0
    
    for i in range (n,m):
        result = result + i

    return(result)
    
print(cal_sigma(1,999))

#Calculating pi
def cal_pi(n,m):
    
    result = 1
    
    for i in range (n,m+1):
        result = result * i
    return (result)
    
print(cal_pi(1,6))

#Exercise 3: Recurser Function
def cal_f(m):
    if m == 0:
        return 1
    else:
        return m*cal_f(m-1)
print(cal_f(5))

#Calculating Permutation 
def cal_p(n,m):
    return (cal_f(m)/cal_f(m-n))
    
print(cal_p(3,5))
    