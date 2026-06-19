##### wehile loops #######
i = 1 
while i < 6:
    print(i)
    if (i==4):
        break
    i += 1  

##### continew state ment ####

i = 0
while i<7:
    i += 1
    if i == 3 : 
        continue
    print (i)

### if - else in whil loops ###

i = 1
while i< 5:
    print(i)
    i += 1
else : 
    print(" i is no longer less than 5")




########## print 0-10  for loops ###
##########
for x in range(11):
    print(x)

##########  print loop ###

fruits= ["mango", "apple" , "banana" ]
print(fruits)

#### break loops ######


fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break





######### TASK -6 DAY -5  star pattern ##########
for i in range(1, 6):
    print("*" * i)



####### star pattern reverse ##########
for i in range (6,1,-1):
    print("*" * i)


for i in range (1,0,-1):
    print("*" * i)



###### ptint form user pettrrn #######
start= int(input(" enter the start  value : "))
end=int(input(" enter the ending value "))
for i in range (start ,end + 1 ):
    print("*" * i)


#### for i in range(1, 5):
for i in range(1,6):
    for k in range(1,i+1):
        print(k,end="")
    print()    



    
############   funcation ##########

def star_pettern(rows):
    for i in range(1,rows+ 1 ):
        print("*" *i)

    for i in range(rows-1,0,-1):
      print("*" * i)        

n = int(input("enter the number of rose :  "))
star_pettern(n)    




