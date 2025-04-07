import sqllite3

conn = sqllite3.connect('myClass')


INSERT INTO student(ID, name, age, grade, gpa)
VALUES (1, Evan, 15, 10, 3.2)