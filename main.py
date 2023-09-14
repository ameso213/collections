#change 80 to 89 in the list
student_marks=[60,80,90,98]
student_marks[1]=89
student_marks[1]=89
print(student_marks)


#append 55 to the list(add a new file)
student_marks=[60,89,90,98]
student_marks.append(55)
print(student_marks)


#find the size of the list after appending 55
print(len(student_marks))


#write a python program to sum all the items in the list
#total of items
student_marks=[60,89,90,98,55]
total=sum(student_marks)
print(total)


#write a python function that takes two lists and return true if they have at least one common member
list1=input("enter list1:")
list2=input("enter list2:")
if list1 and list2:
    print("yes,has a common member")
else:
    print("no,has no member")  
    
