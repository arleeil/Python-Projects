student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]


max_score= 0
lowest_score =0

for x in student_scores:
    if x > max_score:
        max_score = x
    if x<max_score:
        lowest_score = x
print(f'Maximum score = {max_score} and Minimum score = {lowest_score}')

summ = 0
for y in student_scores:
    summ+=y
print(f'Your Total: {summ}')
