#Iterating over only part of a list
numbers=[2,4,6,8,7,10,11,14,16,18,20,23,22,25]

for items in numbers[:5]:
    print(items)


print()
#for loop with enumerate
to_do_task=["prepare_ppt", "complete_assignment", "bring_groceries","have_food"]

for index, tasks in enumerate(to_do_task):
    print(f"Task {index} : {tasks}")


print()
#iterating through dictionary
grades={"abhi": 80, "raj":'75', "nag": 80, "yash": 65}

for student_name, percentage in grades.items():
    print(f"student name: {student_name} and grade is {percentage}")


print()

for lis in grades:
    print(f"student name: {lis} and grade is {grades[lis]}")
print()



#iterating through strings
name = "learning"

for char in name:
    print(f"current character is : {char}")

print()

#iterating through list of integers

numbers_lis=[1,3,4,5,6,7,8,9]

for item in numbers_lis:
    print(f"current value is {item}")

print()

