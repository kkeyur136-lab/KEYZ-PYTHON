def my_petten():
    row=int(input("enter the value : ") )
    i = 1
    while i<= row :
          print("*"*i)
          i += 1 
my_petten()            #### logic is  :- when using ehile loop in thair to user
                                        i- ( #### input) = 1
                                        ######  i <= row means :- row is similer with input  or bigeer then input 
                                        ### print ("*" * i )same as wall as range 
                                        ## i += 1 
                                      #### last print funtion ok

#### logic in loops use in this petten formate ####
def my_petten():
    row=int(input("enter the value : ") )
    i = 1
    while i<= row :
          print("*"*i)
          i += 1 
my_petten()     ######### normal with using while  ####



#### new thing as 1 -22-333-444 for 


def my_pattern():
    row = int(input("Enter the value: "))

    i = 1
    while i <= row:
        print(i * str(i))
        i += 1             ###  using i * str(i) : print :-   1-22-333-4444*** 

my_pattern()


#### print 1-12-123 
row = int(input("enter the row : "))   ### simple lline add user :

i = 1 
while i <= row :      ## normal with while 
     j =1              ## add one mre funcation ike j ,k ,l       
     while j <= i :     ### add thod while  :
          print(j,end="")    #### (j,end="")  in last 
          j +=1               ### AS IT IS i in j  j += 1 
     print()
     i+=1                      ########## add one more funtion is print 1-12-123 
                                           
                                      