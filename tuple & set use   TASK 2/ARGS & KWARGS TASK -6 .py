def my_funtion(*args):
    print("type",type(args))
    print("first rgument : ", args[0])
    print("second argument :",args[1])
    print("all arguments : ", args)
my_funtion("emil","tobias","linus")

#################################
def my_function(*numbers):
  total = 0
  for num in numbers:
    total += num
  return total

print(my_function(1, 2, 3))
print(my_function(10, 20, 30, 40))
print(my_function(5))

#### using lembda funtion ####
def myfunc(n):
   return lambda a : a * n
mydoubler = myfunc(2)
mytripler=myfunc(3) 

print(mydoubler(11))
print(mytripler(11))

##### fectorial using ###
def factorial(n):
  # Base case
  if n == 0 or n == 1:
    return 1
  # Recursive case
  else:
    return n * factorial(n - 1)

print(factorial(5))

####### golbal fiuntion 
#############

x = "global"

def outer():
  x="enclosing "
  def inner():
    x= "local"
    print("inner:",x)
    inner()
    print("outer:", )
outer()
print("global:",x)

