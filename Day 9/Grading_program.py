student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades={}

for student in student_scores :
    
    score=student_scores[student]
    
    if score>=91:
        student_grades[student]='Outstanding'
    if score>=81 and score<90:
        student_grades[student]='Exceeds Expectations'
    if score>=71 and score<80:
        student_grades[student]='Acceptable' 
    if score<70:
        student_grades[student]='Fail'

print(student_grades)
