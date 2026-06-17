##tuple's###
mytuple=(1,2,3,4,5,6,)
print(mytuple)


###COVERT IN LIST ###
mytuple=(1,2,3,4,5,6,)
mylist=list(mytuple)
print(mylist)


### add value in tuple ###
mytuple=("keyz","kathan","bapu")
A=list(mytuple)
A.append("dev")
mytupl=tuple(A)
print(mytuple)

### delete the tuple###
mytuple=("keyz","kathan","bapu")
A=list(mytuple)
A.append("dev")
mytupl=tuple(A)
del mytuple
print()

##### nested tuple ###
mytuple=(1,2,3,4,5,6,(7,8,9))
print(mytuple)




###########################   SEt functions ###########################


myset={1,2,3,4,5,6,}
print(myset)


##### #add in set ###
myset={"keyur","kathan","bapu"}
myset.add("dev")
print(myset)

## check value in set##
myset={"keyur","kathan","bapu"}
print("keyur" in myset )

###### not availabale in set ###
myset ={"keyur","kathan","bapu"}
print("dev" not in myset )

##### convert in tuple##
myset ={"keyur","kathan","bapu"}
mytuple=tuple(myset)
print(mytuple)
myset=type(mytuple)
print(myset)

######## delete one value in set#####
myset ={"keyur","kathan","bapu"}
myset.remove("bapu")
print(myset )


#############delet set ######
myset ={"keyur","kathan","bapu"}
myset.clear()
print(myset)


### add set in set ####
myset1 ={"keyur","kathan","bapu"}
myset2={"nandini","pachi","priti"}
myset1.update(myset2)
print(myset1)

#### create nested set#########
myset ={"keyur","kathan","bapu"}
myset1={"nandini","prachi","priti"}
myset2=myset.union(myset1)
print(myset2)




###### JOINE SET ####
##tuple's###
mytuple=(1,2,3,4,5,6,)
print(mytuple)


###COVERT IN LIST ###
mytuple=(1,2,3,4,5,6,)
mylist=list(mytuple)
print(mylist)


### add value in tuple ###
mytuple=("keyz","kathan","bapu")
A=list(mytuple)
A.append("dev")
mytupl=tuple(A)
print(mytuple)

### delete the tuple###
mytuple=("keyz","kathan","bapu")
A=list(mytuple)
A.append("dev")
mytupl=tuple(A)
del mytuple
print()

##### nested tuple ###
mytuple=(1,2,3,4,5,6,(7,8,9))
print(mytuple)




###########################   SEt functions ###########################


myset={1,2,3,4,5,6,}
print(myset)


##### #add in set ###
myset={"keyur","kathan","bapu"}
myset.add("dev")
print(myset)

## check value in set##
myset={"keyur","kathan","bapu"}
print("keyur" in myset )

###### not availabale in set ###
myset ={"keyur","kathan","bapu"}
print("dev" not in myset )

##### convert in tuple##
myset ={"keyur","kathan","bapu"}
mytuple=tuple(myset)
print(mytuple)
myset=type(mytuple)
print(myset)

######## delete one value in set#####
myset ={"keyur","kathan","bapu"}
myset.remove("bapu")
print(myset )


#############delet set ######
myset ={"keyur","kathan","bapu"}
myset.clear()
print(myset)


### add set in set ####
myset1 ={"keyur","kathan","bapu"}
myset2={"nandini","pachi","priti"}
myset1.update(myset2)
print(myset1)

#### create nested set#########
myset ={"keyur","kathan","bapu"}
myset1={"nandini","prachi","priti"}
myset2=myset.union(myset1)





#####################  TASK 2 :###################
##### crate a sets  :: set1,2,3\
###   symmetric diffreance ##  z = x ^ y
####   diffreance  ##  " - "
## intersection " &" ####
#### union " | "


## 1- create set : set 1- set 2 #####
myset1 ={"keyur","kathan","bapu"}
myset2={"nandini","prachi","priti"}
print(myset1 - myset2 )


#### 2 - symmetric diffrances ########
myset1 ={"keyur","kathan","bapu","nandini"}
myset2={"nandini","prachi","priti","keyur"}

myset3 = myset1.symmetric_difference(myset2)
print(myset3)


######### diffrances ########
myset1 ={"keyur","kathan","bapu","nandini"}
myset2={"nandini","prachi","priti","keyur"}
myset3 = myset1 ^ myset2 
print(myset3)

##### 4- intersenction #####
myset1 ={"keyur","kathan","bapu","nandini"}
myset2={"nandini","prachi","priti"}
myset3= myset1 & myset2
print(myset3)

############# union #######
myset1 ={"keyur","kathan","bapu","nandini"}
myset2={"nandini","prachi","priti","keyur"}

myset3 = myset1  | myset2 
print(myset3)
