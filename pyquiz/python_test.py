x=[100,110,120,130,140,150]
y=[n*5 for n in x]
print(y)

#2
def divisible_by_three(n):
    for num in range(1,n+1):
        if num%3==0:
            print(num)
divisible_by_three(50)            


# 3. 
def flatterns_list(x):    
   new_list= [item for sublist in x for item in sublist]
   return new_list
x=flatterns_list([[1,2],[3,4],[5,6]]) 
print(x)   

# 4.
def smallest(x):
    return min (x)
print(smallest([3,6,8,2,4,1,5,7]))

def greeting(student_list):
    for num in student_list:
        birth_year=2021-num["age"]
        name=num["name"]
        print(f"Hello {name} you were born in the year {birth_year}")

greeting([{"age": 19, "name": "Eunice"}]) 
 


# 5
def sort_list(x):

    new_set=set(x)
    return list(new_set)
print(sort_list(['a','b','a','e','d','b','c','e','f','g','h']))


# 6. 
def divisible_by_seven():
    my_list=[]
    for items in range(100,201):
        if items%7==0:
            my_list.append(items)
    return my_list
x=divisible_by_seven()
print(x)   


#6
def divisible_seven(number):
    range(100,200)
    for number in range :
        if number%7==0:
            return f"divisible by seven"
        else:
            return f"other numbers"
divisible_seven(100,200)








 


