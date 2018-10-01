import json
class CS_Class(object):
	def read_file(self, name):
		"""
		This def's only function is reading the file it was given and returns the data contents in the file.
		"""
		with open(name) as f: # open the selected file
			data = json.loads(f.read()) #place teh file's data into a variable
		return data #send the data filled variable out
	def count_male(self, data):
		"""
		The only function of this function is to count all the male students in the data.
		"""
		males=0#variable/counter
		for i in range(len(data)):#Look through the data
			if (data[i][1]=='M'):#find all students labelled as male
				males += 1#incriment the counter by 1
		#print ("There are %i males in the database.\n" % (males))
		return males
	def count_female(self, data):
		"""
		The only function of this function is to count all the female students in the data.
		"""
		females = 0 #variable/counter
		for i in range(len(data)): #Look through the data
			if (data[i][1]=='F'): #find all students labelled as female
				females += 1 #incriment the counter by 1
		#print ("There are %i females in the database.\n" % (females))
		return females
	def grades_m(self, data):
		"""
		Find all the midterm grades of every student in the data file. Seperate the grades into another variable/list.
		"""
		midterm = [] # Empty list
		for i in range(len(data)): # go through the data list
			midterm.append(str(data[i][2])) #add every midterm grade into the midterm list
		return midterm
	def grades_f(self, data):
		"""
		Find all the final grades of every student in the data file. Seperate the grades into another variable/list.
		"""
		final = []#empty list
		for i in range(len(data)):# go through the data list
			final.append(str(data[i][3]))#add every final grade into the midterm list
		return final
	def grades_count_m(self, mid):
		"""
		Count all the midterm letter grade into counters
		"""
		counter_mid = {'A':0,'B':0,'C':0,'D':0,'F':0} #all letter grade counter starting at zero
		for i in range(len(mid)): #go through the range of the midterm list
			counter_mid[mid[i]] += 1 #incriment the midterm counter list by one based on the letter grade
		#print ("This is the midterm grade count: %s." % (str(counter_mid)))
		return counter_mid
	def grades_count_f(self, final):
		"""
		Count all the final letter grade into counters
		"""
		counter_final = {'A':0,'B':0,'C':0,'D':0,'F':0}#all letter grade counter starting at zero
		for i in range(len(final)):#go through the range of the final list
			counter_final[final[i]] += 1#incriment the final counter list by one based on the letter grade
		#print ("This is the final grade count: %s." % (str(counter_final)))
		return counter_final
	def grade_avg_m(self, midterm):
		"""
		Grade the average grade of the overall class.
		"""
		points = {'A':5,'B':4,'C':3,'D':2,'F':1} #Determine the points the class gets based on student midterm grade
		average = {5:'A',4:'B',3:'C',2:'D',1:'F'} #Determine the overall grade of the class
		count_m = 0#counte where all points are added up
		for i in range(len(midterm)):#go through the entire midterm list
			count_m += points[midterm[i]] #add the points up
		count_m = average[int(count_m/len(midterm))]#Get the average of the overall points and interger the value to compare to the average class grade.
		#print ("The average class grade for midterm is %s." % (count_m))
		return count_m
	def grade_avg_f(self, final):
		"""
		Grade the average grade of the overall class.
		"""
		points = {'A':5,'B':4,'C':3,'D':2,'F':1} #Determine the points the class gets based on student midterm grade
		average = {5:'A',4:'B',3:'C',2:'D',1:'F'} #Determine the overall grade of the class
		count_f = 0#counte where all points are added up
		for i in range(len(final)):#go through the entire final list
			count_f += points[final[i]]#go through the entire final list
		count_f = average[int(count_f/len(final))]#Get the average of the overall points and interger the value to compare to the average class grade.
		#print ("The average class grade for final is %s." % (count_f))
		return count_f
	def average_change(self, midterm, final):
		"""
		Find the average letter grade change in the class overall from midterm to final. Did the class's overall students improve or worsen? And by how much?
		"""
		points = {'A':2,'B':1,'C':0,'D':-1,'F':-2} #If it is above C it is a positive grade, of below C it is a negative grade and C is a neutral grade.
		change = 0 # ewmpty counter list
		for i in final:
			change += abs(int((final[i]-midterm[i]))*points[i]) #grab the letter grade change from midterm to final and multiple the points to it
		return change
