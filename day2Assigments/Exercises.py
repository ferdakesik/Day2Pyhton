### Exercise 1 
#Given a list as a parameter,write a function that returns a list of numbers that are less than ten
#For example: Say your input parameter to the function is [1,11,14,5,8,9]...Your output should [1,5,8,9]

def lessTen(number):
    
        return [num for num in number if num<10]

number=[1,34,22,11,5,3,2]
result=lessTen(number)
print(result)


#### Exercise 2 
#Write a function that takes in two lists and returns the two lists merged together and sorted
#Hint: You can use the .sort() method
##l_1 = [1,2,3,4,5,6]
##l_2 = [3,4,5,6,7,8,10]

def combinedSort(list1,list2):
    combined=list1 + list2
    sortedLists=sorted(combined)
    return sortedLists

list1=[3,1,6,7,8,9,12,34]
list2=[4,5,8,99,45,2]

result=combinedSort(list1,list2)
print(result)