"""reducer.py"""
# fill in code
import sys
import numpy as np

maths_grades =   []
earth_grades =   []
history_grades = []
top_math = []
top_earth = []
top_hist = []

f = sys.stdin

for text in f:

	line = text.strip()
	course,grade,name = line.split('\t')

	grade=int(grade)

	if course=='Mathematics':
		maths_grades.append(grade)
		top_math.append([name,grade])

	elif course=='Earth Science':
		earth_grades.append(grade)
		top_earth.append([name,grade])
	
	elif course=='History':
		history_grades.append(grade)
		top_hist.append([name,grade])
 
maths_avg = np.round(np.average(maths_grades),decimals=3)
earth_avg = np.round(np.average(earth_grades),decimals=3)
history_avg = np.round(np.average(history_grades),decimals=3)

sorted_math_grade = sorted(top_math, key=lambda x: x[1], reverse=True)
sorted_earth_grade = sorted(top_earth, key=lambda x: x[1], reverse=True)
sorted_hist_grade = sorted(top_hist, key=lambda x: x[1], reverse=True)
    
print'maths average grade:',maths_avg;
print'\nearth sciences average grade:',earth_avg;
print'\nhistory average grade:',history_avg

print'\ntop 5 maths students:'
for i in range(0,5):
	print sorted_math_grade[i][0] + '\t'+str(sorted_math_grade[i][1])

print'\ntop 5 earth science students:'
for i in range(0,5):
	print sorted_earth_grade[i][0] +'\t'+str(sorted_earth_grade[i][1])

print'\ntop 5 history students:'
for i in range(0,5):
	print sorted_hist_grade[i][0] + '\t'+str(sorted_hist_grade[i][1])


