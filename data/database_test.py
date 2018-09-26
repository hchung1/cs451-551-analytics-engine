import json
class CS_Class(object):
	def read_file(self, name):
		with open(name) as f:
			data = json.loads(f.read())
		return data
	def count_male(self, data):
		males=0
		for i in range(len(data)):
			if (data[i][1]=='M'):
				males += 1
		#print ("There are %i males in the database.\n" % (males))
		return males
	def count_female(self, data):
		females = 0
		for i in range(len(data)):
			if (data[i][1]=='F'):
				females += 1
		#print ("There are %i females in the database.\n" % (females))
		return females
	def grades_m(self, data):
		midterm = []
		for i in range(len(data)):
			midterm.append(str(data[i][2]))
		return midterm
	def grades_f(self, data):
		final = []
		for i in range(len(data)):
			final.append(str(data[i][3]))
		return final
	def grades_count_m(self, mid):
		counter_mid = {'A':0,'B':0,'C':0,'D':0,'F':0}
		for i in range(len(mid)):
			counter_mid[mid[i]] += 1
		#print ("This is the midterm grade count: %s." % (str(counter_mid)))
		return counter_mid
	def grades_count_f(self, final):
		counter_final = {'A':0,'B':0,'C':0,'D':0,'F':0}
		for i in range(len(final)):
			counter_final[final[i]] += 1
		#print ("This is the final grade count: %s." % (str(counter_final)))
		return counter_final
	def grade_avg_m(self, midterm):
		points = {'A':5,'B':4,'C':3,'D':2,'F':1}
		average = {5:'A',4:'B',3:'C',2:'D',1:'F'}
		count_m = 0
		for i in range(len(midterm)):
			count_m += points[midterm[i]]
		count_m = average[int(count_m/len(midterm))]
		#print ("The average class grade for midterm is %s." % (count_m))
		return count_m
	def grade_avg_f(self, final):
		points = {'A':5,'B':4,'C':3,'D':2,'F':1}
		average = {5:'A',4:'B',3:'C',2:'D',1:'F'}
		count_f = 0
		for i in range(len(final)):
			count_f += points[final[i]]
		count_f = average[int(count_f/len(final))]
		#print ("The average class grade for final is %s." % (count_f))
		return count_f
	def average_change(self, midterm, final):
		points = {'A':2,'B':1,'C':0,'D':-1,'F':-2}
		change = 0
		for i in final:
			change += int((final[i]-midterm[i])*points[i])
		return change
