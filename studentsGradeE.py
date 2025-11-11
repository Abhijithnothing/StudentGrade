import sys

if len(sys.argv)==6:
    script_name=sys.argv[0]
    marks1=sys.argv[1]
    marks2=sys.argv[2]
    marks3=sys.argv[3]
    marks4=sys.argv[4]
    marks5=sys.argv[5]

else:
    script_name=sys.argv[0]
    marks1=99
    marks2=99
    marks3=99
    marks4=99
    marks5=99
    print("Input marks not provided, using default marks")


total_marks=int(marks1)+int(marks2)+int(marks3)+int(marks4)+int(marks5)
average_marks=total_marks/5

if average_marks>=90:
    grade="A"
elif average_marks>=70:
    grade="B"
elif average_marks>=50:
    grade="C"
elif average_marks>=35:
    grade="D"
else:
    grade="F"


print("Script Name:",script_name)
print("Total Marks:",total_marks)
print("Average Marks:",average_marks)   
print("Grade:",grade)