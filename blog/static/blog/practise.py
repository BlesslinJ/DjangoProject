

'''def check_prime(num):
	for i in range(2,num):
		if num%i == 0:
			return False
	return True
	

if check_prime(24):
	print("True") 
else:
    print("false")	'''

'''def generate_fibonacci():
	list1=[]
	a=0
	b=1
	c=a+b
	list1=[a,b,c]
	for i in range(10):
		a=b
		b=c
		c=a+b
		list1.append(c)
	print(list1)

generate_fibonacci()'''

'''# python program to check if x is a perfect square 
import math 
  
# A utility function that returns true if x is perfect square 
def isPerfectSquare(x): 
    s = int(math.sqrt(x)) 
    return s*s == x 
  
# Returns true if n is a Fibinacci Number, else false 
def isFibonacci(n): 
  
    # n is Fibinacci if one of 5*n*n + 4 or 5*n*n - 4 or both 
    # is a perferct square 
    return isPerfectSquare(5*n*n + 4) or isPerfectSquare(5*n*n - 4) 
     
# A utility function to test above functions 
for i in range(1,11): 
     if (isFibonacci(i) == True): 
         print i,"is a Fibonacci Number"
     else: 
         print i,"is a not Fibonacci Number "'''

'''def div_all(num):
    for each in str(num):
        if num%int(each) ==0:
           f = True
        else:
           return False
    return f  
    
print(div_all(130)) '''

'''each = 130
list1 = [x for x in str(each) if int(x) != 0 and each%int(x) == 0 ]  
if len(list1) == len(str(each)):
   print('True') '''

'''def check_palindrome(num):
    str_num = str(num)
    str_rev = str_num[::-1]
    if str_num == str_rev:
       return True
    else:
       return False

print(check_palindrome(1233351)) '''

'''import math
def check_armstrong(num):
    length = len(str(num))  
    total = 0 
    for each in str(num):
    	no = pow(int(each),length)	
    	total+=no
    	print(total)
    return total

numb=153
if numb == check_armstrong(153):
   print('true')
else:
   print('false')'''

'''import re 
  
# initialising string 
ini_string = "123()#$ABGFD5abcjw"
ini_string2 = "abceddfgh"
  
# printing strings 
print ("initial string : ", ini_string, ini_string2) 
  
# code to find characters in string 
res1 = " ".join(re.split("[^a-zA-Z]*", ini_string)) 
res2 = " ".join(re.split("[^a-zA-Z]*", ini_string2)) 
  
# printing resultant string 
print ("first string result: ", str(res1)) 
print ("second string result: ", str(res2)) '''         

# Function for nth fibonacci number - Space Optimisataion 
# Taking 1st two fibonacci numbers as 0 and 1 
'''  
def fibonacci(n): 
    a = 0
    b = 1
    if n < 0: 
        print("Incorrect input") 
    elif n == 0: 
        return a 
    elif n == 1: 
        return b 
    else: 
        for i in range(2,n): 
            c = a + b 
            a = b 
            b = c 
        return b 
'''

test_tup1 = ('GFG', 'is', 'best') 
test_tup2 = (1, 2, 3) 
  
for each in test_tup1:
	print(each)
# printing original tuples 
print("The original key tuple is : " + str(test_tup1)) 
print("The original value tuple is : " + str(test_tup2)) 
  
# Using Dictionary Comprehension 
# Convert Tuples to Dictionary 
res = {test_tup1[i] : test_tup2[i] for i in range(len(test_tup2))} 
  
# printing result  
print("Dictionary constructed from tuples : " + str(res)) 



































