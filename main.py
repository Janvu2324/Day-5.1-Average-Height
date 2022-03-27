# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
print(student_heights)
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

total_height = 0
for i in student_heights:
  total_height=i+total_height

number_student = 0
for i in student_heights:
  number_student=number_student+1


Average= total_height / number_student

print(f'Average of student height is : {round(Average)}')
  
  




