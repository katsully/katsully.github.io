import csv

with open('grading/Sheet1.csv', 'r') as infile:
	reader = csv.reader(infile)
	first_line = True
	for row in reader:
		if first_line:
			headers = row
			first_line = False
			continue
		homeworks = []
		hw_list = ""
		quizzes = 0
		q_count = 0
		q_list = ""
		class_participation = 10
		absences = 0
		tardies = 0
		midterm = 0
		final = 0
		if row[0].rfind(' ') != -1:
			n = "".join(row[0].split(" ")[:2][::-1]).replace(',','')
		# else: 
		# 	n = row[0].split(' ')[0]
		name = ''.join(n.split(',')[::-1])
		student_file = open("grading/" + name + ".txt", 'w')
		student_file.write("Name: " + ' '.join(n.split(',')[::-1]) + "\n")
		student_file.write("Github: " + row[1] + "\n")
		for idx,r in enumerate(row):
			if r:
				if "Homework" in headers[idx]:
					if r == '-':
						continue
					homeworks.append(int(r))
					hw_list += headers[idx] + ": " + r + "\n"
				if "Quiz" in headers[idx]:
					if r == '-':
						continue
					quizzes += float(r)
					q_count += 1
					q_list += headers[idx] + ": " + r + "\n"
				if "Week" in headers[idx]:
					if r == 't':
						tardies += 1
					elif r == 'a':
						absences += 1
				if "Midterm" in headers[idx]:
					midterm = float(r)
				if "Final" in headers[idx]:
					final = float(r)
		
		#drop lowest homework
	#	homeworks.remove(min(homeworks))

		student_file.write("\n" + q_list)
		if q_count > 0:
			quiz_grade = round(quizzes/q_count)
		else:
			quiz_grade = 0
		hw_grade = round(sum(homeworks)/len(homeworks))
		student_file.write("Quiz Grade: " + str(quiz_grade) + "\n")
		student_file.write("\n" + hw_list)
		# student_file.write("Homework Grade (with lowest grade dropped): " + str(hw_grade) + "\n")
		student_file.write("Homework Grade: " + str(hw_grade) + "\n")
		student_file.write("\nClass Participation: 100" + "\n")
		# student_file.write("\nClass Participation: " + str(class_participation*10) + "\n")

		# student_file.write("\nMidterm Grade: " + str(midterm) + "\n")

		# student_file.write("\nFinal Grade: " + str(final) + "\n")

		student_file.write("\nStudents are allowed one unexcused absence, after that each absence results in a grade deduction.")
		student_file.write("\nThree tardies will result in an unexcused absence.")

		deduction = 0
		if absences > 0:
			deduction += (absences - 1)
		deduction += int(tardies/3)

		if absences > 0:
			student_file.write("\nTotal unexcused absences: " + str(absences-1))
		else:
			student_file.write("\nTotal unexcused absences: 0")


		student_file.write("\nTotal tardies: " + str(tardies))
		student_file.write("\nGrade deductions: " + str(deduction))


		#grade = math.ceil((quiz_grade * .15) + (hw_grade * .4) + class_participation + (midterm * .15) + (final * .2) - (deduction))
		grade = round((quiz_grade * .15) + (hw_grade * .4) + class_participation - (1.5*deduction))
		grade1 = round(grade + 35)
		grade2 = round(grade + (35 * .8))
		# grade1 = math.ceil(grade + 20)
		# grade2 = math.ceil(grade + (20 * .8))

		student_file.write("\n\nPotential grade if you get 100% on the midterm and final: " + str(grade1))
		student_file.write("\nPotential grade if you get 80% on the midterm and final: " + str(grade2))

		# student_file.write("\n\nPotential grade if you get a 100 on the final: " + str(grade1))
		# student_file.write("\nPotential grade if you get a 80 on the final: " + str(grade2))

		# student_file.write("\nYOUR FINAL GRADE: " + str(grade))
		
		student_file.write("\n\nPlease note, class participation will not be an automatic 100 moving forward in the semester. Also, there will be more quizzes and homeworks that can also improve your final grade. Feel free to email me with any comments, questions, or concerns.")
		student_file.close()

infile.close()
