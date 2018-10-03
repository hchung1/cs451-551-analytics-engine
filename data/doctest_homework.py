import doctest
import json
def read_file(name):
	"""
	This def's only function is reading the file it was given and returns the data contents in the file.
	>>> read_file('grade-data.json')
	[[u'F2008', u'M', u'F', u'F'], [u'F2013', u'M', u'C', u'B'], [u'F2013', u'F', u'A', u'A'], [u'F2013', u'M', u'B', u'A'], [u'S2018', u'M', u'B', u'B'], [u'F2013', u'F', u'C', u'A'], [u'F2012', u'M', u'B', u'A'], [u'F2008', u'M', u'D', u'B'], [u'S2010', u'M', u'C', u'F'], [u'S2011', u'M', u'B', u'A'], [u'F2013', u'M', u'F', u'F'], [u'F2014', u'M', u'B', u'B'], [u'F2014', u'M', u'A', u'A'], [u'S2016', u'M', u'F', u'F'], [u'F2012', u'F', u'A', u'A'], [u'F2012', u'F', u'A', u'A'], [u'S2016', u'F', u'B', u'B'], [u'S2016', u'M', u'A', u'A'], [u'S2010', u'F', u'C', u'B'], [u'F2013', u'F', u'A', u'A'], [u'F2008', u'M', u'B', u'A'], [u'F2011', u'M', u'C', u'A'], [u'S2016', u'M', u'A', u'A'], [u'F2017', u'M', u'B', u'B'], [u'S2018', u'M', u'B', u'B'], [u'F2015', u'M', u'A', u'A'], [u'F2013', u'M', u'C', u'B'], [u'S2011', u'M', u'A', u'A'], [u'F2009', u'M', u'C', u'B'], [u'F2010', u'M', u'C', u'C'], [u'F2012', u'M', u'A', u'A'], [u'F2012', u'M', u'B', u'C'], [u'F2013', u'M', u'C', u'D'], [u'F2013', u'M', u'F', u'F'], [u'F2013', u'M', u'B', u'A'], [u'F2009', u'M', u'A', u'A'], [u'F2014', u'M', u'C', u'C'], [u'S2012', u'M', u'A', u'A'], [u'F2015', u'M', u'C', u'D'], [u'S2014', u'M', u'B', u'B'], [u'S2011', u'M', u'B', u'A'], [u'F2008', u'M', u'D', u'C'], [u'S2012', u'F', u'A', u'A'], [u'S2016', u'M', u'C', u'C'], [u'F2015', u'M', u'C', u'C'], [u'F2013', u'M', u'B', u'A'], [u'F2013', u'F', u'A', u'A'], [u'S2015', u'M', u'A', u'A'], [u'F2009', u'F', u'B', u'A'], [u'S2016', u'M', u'C', u'C'], [u'F2008', u'M', u'C', u'B'], [u'F2015', u'M', u'A', u'A'], [u'S2018', u'M', u'C', u'F'], [u'F2008', u'M', u'A', u'A'], [u'S2018', u'M', u'A', u'B'], [u'S2014', u'M', u'A', u'A'], [u'S2014', u'M', u'A', u'A'], [u'F2008', u'M', u'C', u'A'], [u'S2014', u'M', u'A', u'B'], [u'F2011', u'F', u'A', u'A'], [u'F2015', u'M', u'B', u'C'], [u'F2013', u'M', u'C', u'C'], [u'F2012', u'M', u'F', u'C'], [u'F2014', u'M', u'B', u'A'], [u'F2015', u'M', u'C', u'C'], [u'S2016', u'M', u'B', u'B'], [u'F2014', u'M', u'B', u'C'], [u'F2012', u'M', u'A', u'A'], [u'F2010', u'M', u'F', u'B'], [u'S2012', u'M', u'A', u'A'], [u'S2017', u'M', u'B', u'B'], [u'S2015', u'M', u'B', u'B'], [u'S2009', u'M', u'C', u'A'], [u'F2008', u'M', u'C', u'B'], [u'S2014', u'M', u'A', u'B'], [u'F2013', u'F', u'A', u'A'], [u'S2016', u'M', u'A', u'A'], [u'F2015', u'M', u'C', u'C'], [u'S2014', u'F', u'D', u'B'], [u'F2009', u'M', u'B', u'A'], [u'F2010', u'M', u'A', u'A'], [u'S2009', u'F', u'C', u'B'], [u'F2015', u'F', u'C', u'B'], [u'S2010', u'M', u'B', u'A'], [u'S2014', u'M', u'A', u'A'], [u'S2010', u'F', u'B', u'B'], [u'F2008', u'M', u'C', u'B'], [u'F2008', u'F', u'B', u'A'], [u'F2009', u'M', u'B', u'A']]
	"""
	with open(name) as f:
		data = json.loads(f.read())
	return data
def gender(data):
	"""
	>>> gender([[u'F2008', u'M', u'F', u'F'], [u'F2013', u'M', u'C', u'B'], [u'F2013', u'F', u'A', u'A'], [u'F2013', u'M', u'B', u'A'], [u'S2018', u'M', u'B', u'B'], [u'F2013', u'F', u'C', u'A'], [u'F2012', u'M', u'B', u'A'], [u'F2008', u'M', u'D', u'B'], [u'S2010', u'M', u'C', u'F'], [u'S2011', u'M', u'B', u'A'], [u'F2013', u'M', u'F', u'F'], [u'F2014', u'M', u'B', u'B'], [u'F2014', u'M', u'A', u'A'], [u'S2016', u'M', u'F', u'F'], [u'F2012', u'F', u'A', u'A'], [u'F2012', u'F', u'A', u'A'], [u'S2016', u'F', u'B', u'B'], [u'S2016', u'M', u'A', u'A'], [u'S2010', u'F', u'C', u'B'], [u'F2013', u'F', u'A', u'A'], [u'F2008', u'M', u'B', u'A'], [u'F2011', u'M', u'C', u'A'], [u'S2016', u'M', u'A', u'A'], [u'F2017', u'M', u'B', u'B'], [u'S2018', u'M', u'B', u'B'], [u'F2015', u'M', u'A', u'A'], [u'F2013', u'M', u'C', u'B'], [u'S2011', u'M', u'A', u'A'], [u'F2009', u'M', u'C', u'B'], [u'F2010', u'M', u'C', u'C'], [u'F2012', u'M', u'A', u'A'], [u'F2012', u'M', u'B', u'C'], [u'F2013', u'M', u'C', u'D'], [u'F2013', u'M', u'F', u'F'], [u'F2013', u'M', u'B', u'A'], [u'F2009', u'M', u'A', u'A'], [u'F2014', u'M', u'C', u'C'], [u'S2012', u'M', u'A', u'A'], [u'F2015', u'M', u'C', u'D'], [u'S2014', u'M', u'B', u'B'], [u'S2011', u'M', u'B', u'A'], [u'F2008', u'M', u'D', u'C'], [u'S2012', u'F', u'A', u'A'], [u'S2016', u'M', u'C', u'C'], [u'F2015', u'M', u'C', u'C'], [u'F2013', u'M', u'B', u'A'], [u'F2013', u'F', u'A', u'A'], [u'S2015', u'M', u'A', u'A'], [u'F2009', u'F', u'B', u'A'], [u'S2016', u'M', u'C', u'C'], [u'F2008', u'M', u'C', u'B'], [u'F2015', u'M', u'A', u'A'], [u'S2018', u'M', u'C', u'F'], [u'F2008', u'M', u'A', u'A'], [u'S2018', u'M', u'A', u'B'], [u'S2014', u'M', u'A', u'A'], [u'S2014', u'M', u'A', u'A'], [u'F2008', u'M', u'C', u'A'], [u'S2014', u'M', u'A', u'B'], [u'F2011', u'F', u'A', u'A'], [u'F2015', u'M', u'B', u'C'], [u'F2013', u'M', u'C', u'C'], [u'F2012', u'M', u'F', u'C'], [u'F2014', u'M', u'B', u'A'], [u'F2015', u'M', u'C', u'C'], [u'S2016', u'M', u'B', u'B'], [u'F2014', u'M', u'B', u'C'], [u'F2012', u'M', u'A', u'A'], [u'F2010', u'M', u'F', u'B'], [u'S2012', u'M', u'A', u'A'], [u'S2017', u'M', u'B', u'B'], [u'S2015', u'M', u'B', u'B'], [u'S2009', u'M', u'C', u'A'], [u'F2008', u'M', u'C', u'B'], [u'S2014', u'M', u'A', u'B'], [u'F2013', u'F', u'A', u'A'], [u'S2016', u'M', u'A', u'A'], [u'F2015', u'M', u'C', u'C'], [u'S2014', u'F', u'D', u'B'], [u'F2009', u'M', u'B', u'A'], [u'F2010', u'M', u'A', u'A'], [u'S2009', u'F', u'C', u'B'], [u'F2015', u'F', u'C', u'B'], [u'S2010', u'M', u'B', u'A'], [u'S2014', u'M', u'A', u'A'], [u'S2010', u'F', u'B', u'B'], [u'F2008', u'M', u'C', u'B'], [u'F2008', u'F', u'B', u'A'], [u'F2009', u'M', u'B', u'A']])
	(72, 17)
	"""
	males=0
	females = 0
	for i in range(len(data)):
		if (data[i][1]=='M'):
			males += 1
		if (data[i][1]=='F'):
			females += 1
	return males, females
def grades(data):
	"""
	>>> grades([[u'F2008', u'M', u'F', u'F'], [u'F2013', u'M', u'C', u'B'], [u'F2013', u'F', u'A', u'A'], [u'F2013', u'M', u'B', u'A'], [u'S2018', u'M', u'B', u'B'], [u'F2013', u'F', u'C', u'A'], [u'F2012', u'M', u'B', u'A'], [u'F2008', u'M', u'D', u'B'], [u'S2010', u'M', u'C', u'F'], [u'S2011', u'M', u'B', u'A'], [u'F2013', u'M', u'F', u'F'], [u'F2014', u'M', u'B', u'B'], [u'F2014', u'M', u'A', u'A'], [u'S2016', u'M', u'F', u'F'], [u'F2012', u'F', u'A', u'A'], [u'F2012', u'F', u'A', u'A'], [u'S2016', u'F', u'B', u'B'], [u'S2016', u'M', u'A', u'A'], [u'S2010', u'F', u'C', u'B'], [u'F2013', u'F', u'A', u'A'], [u'F2008', u'M', u'B', u'A'], [u'F2011', u'M', u'C', u'A'], [u'S2016', u'M', u'A', u'A'], [u'F2017', u'M', u'B', u'B'], [u'S2018', u'M', u'B', u'B'], [u'F2015', u'M', u'A', u'A'], [u'F2013', u'M', u'C', u'B'], [u'S2011', u'M', u'A', u'A'], [u'F2009', u'M', u'C', u'B'], [u'F2010', u'M', u'C', u'C'], [u'F2012', u'M', u'A', u'A'], [u'F2012', u'M', u'B', u'C'], [u'F2013', u'M', u'C', u'D'], [u'F2013', u'M', u'F', u'F'], [u'F2013', u'M', u'B', u'A'], [u'F2009', u'M', u'A', u'A'], [u'F2014', u'M', u'C', u'C'], [u'S2012', u'M', u'A', u'A'], [u'F2015', u'M', u'C', u'D'], [u'S2014', u'M', u'B', u'B'], [u'S2011', u'M', u'B', u'A'], [u'F2008', u'M', u'D', u'C'], [u'S2012', u'F', u'A', u'A'], [u'S2016', u'M', u'C', u'C'], [u'F2015', u'M', u'C', u'C'], [u'F2013', u'M', u'B', u'A'], [u'F2013', u'F', u'A', u'A'], [u'S2015', u'M', u'A', u'A'], [u'F2009', u'F', u'B', u'A'], [u'S2016', u'M', u'C', u'C'], [u'F2008', u'M', u'C', u'B'], [u'F2015', u'M', u'A', u'A'], [u'S2018', u'M', u'C', u'F'], [u'F2008', u'M', u'A', u'A'], [u'S2018', u'M', u'A', u'B'], [u'S2014', u'M', u'A', u'A'], [u'S2014', u'M', u'A', u'A'], [u'F2008', u'M', u'C', u'A'], [u'S2014', u'M', u'A', u'B'], [u'F2011', u'F', u'A', u'A'], [u'F2015', u'M', u'B', u'C'], [u'F2013', u'M', u'C', u'C'], [u'F2012', u'M', u'F', u'C'], [u'F2014', u'M', u'B', u'A'], [u'F2015', u'M', u'C', u'C'], [u'S2016', u'M', u'B', u'B'], [u'F2014', u'M', u'B', u'C'], [u'F2012', u'M', u'A', u'A'], [u'F2010', u'M', u'F', u'B'], [u'S2012', u'M', u'A', u'A'], [u'S2017', u'M', u'B', u'B'], [u'S2015', u'M', u'B', u'B'], [u'S2009', u'M', u'C', u'A'], [u'F2008', u'M', u'C', u'B'], [u'S2014', u'M', u'A', u'B'], [u'F2013', u'F', u'A', u'A'], [u'S2016', u'M', u'A', u'A'], [u'F2015', u'M', u'C', u'C'], [u'S2014', u'F', u'D', u'B'], [u'F2009', u'M', u'B', u'A'], [u'F2010', u'M', u'A', u'A'], [u'S2009', u'F', u'C', u'B'], [u'F2015', u'F', u'C', u'B'], [u'S2010', u'M', u'B', u'A'], [u'S2014', u'M', u'A', u'A'], [u'S2010', u'F', u'B', u'B'], [u'F2008', u'M', u'C', u'B'], [u'F2008', u'F', u'B', u'A'], [u'F2009', u'M', u'B', u'A']])
	(['F', 'C', 'A', 'B', 'B', 'C', 'B', 'D', 'C', 'B', 'F', 'B', 'A', 'F', 'A', 'A', 'B', 'A', 'C', 'A', 'B', 'C', 'A', 'B', 'B', 'A', 'C', 'A', 'C', 'C', 'A', 'B', 'C', 'F', 'B', 'A', 'C', 'A', 'C', 'B', 'B', 'D', 'A', 'C', 'C', 'B', 'A', 'A', 'B', 'C', 'C', 'A', 'C', 'A', 'A', 'A', 'A', 'C', 'A', 'A', 'B', 'C', 'F', 'B', 'C', 'B', 'B', 'A', 'F', 'A', 'B', 'B', 'C', 'C', 'A', 'A', 'A', 'C', 'D', 'B', 'A', 'C', 'C', 'B', 'A', 'B', 'C', 'B', 'B'], ['F', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'F', 'A', 'F', 'B', 'A', 'F', 'A', 'A', 'B', 'A', 'B', 'A', 'A', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'B', 'C', 'A', 'C', 'D', 'F', 'A', 'A', 'C', 'A', 'D', 'B', 'A', 'C', 'A', 'C', 'C', 'A', 'A', 'A', 'A', 'C', 'B', 'A', 'F', 'A', 'B', 'A', 'A', 'A', 'B', 'A', 'C', 'C', 'C', 'A', 'C', 'B', 'C', 'A', 'B', 'A', 'B', 'B', 'A', 'B', 'B', 'A', 'A', 'C', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'A'])
	"""
	midterm = []
	final = []
	for i in range(len(data)):
		midterm.append(str(data[i][2]))
		final.append(str(data[i][3]))
	return midterm, final
def grades_count(mid, final):
	"""
	>>> grades_count(['F', 'C', 'A', 'B', 'B', 'C', 'B', 'D', 'C', 'B', 'F', 'B', 'A', 'F', 'A', 'A', 'B', 'A', 'C', 'A', 'B', 'C', 'A', 'B', 'B', 'A', 'C', 'A', 'C', 'C', 'A', 'B', 'C', 'F', 'B', 'A', 'C', 'A', 'C', 'B', 'B', 'D', 'A', 'C', 'C', 'B', 'A', 'A', 'B', 'C', 'C', 'A', 'C', 'A', 'A', 'A', 'A', 'C', 'A', 'A', 'B', 'C', 'F', 'B', 'C', 'B', 'B', 'A', 'F', 'A', 'B', 'B', 'C', 'C', 'A', 'A', 'A', 'C', 'D', 'B', 'A', 'C', 'C', 'B', 'A', 'B', 'C', 'B', 'B'], ['F', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'F', 'A', 'F', 'B', 'A', 'F', 'A', 'A', 'B', 'A', 'B', 'A', 'A', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'B', 'C', 'A', 'C', 'D', 'F', 'A', 'A', 'C', 'A', 'D', 'B', 'A', 'C', 'A', 'C', 'C', 'A', 'A', 'A', 'A', 'C', 'B', 'A', 'F', 'A', 'B', 'A', 'A', 'A', 'B', 'A', 'C', 'C', 'C', 'A', 'C', 'B', 'C', 'A', 'B', 'A', 'B', 'B', 'A', 'B', 'B', 'A', 'A', 'C', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'A'])
	({'A': 29, 'C': 25, 'B': 26, 'D': 3, 'F': 6}, {'A': 43, 'C': 13, 'B': 25, 'D': 2, 'F': 6})
	"""
	counter_mid = {'A':0,'B':0,'C':0,'D':0,'F':0}
	counter_final = {'A':0,'B':0,'C':0,'D':0,'F':0}
	for i in range(len(mid)):
		counter_mid[mid[i]] += 1
		counter_final[final[i]] += 1
	return counter_mid, counter_final
def grade_avg(midterm, final):
	"""
	>>> grade_avg(['F', 'C', 'A', 'B', 'B', 'C', 'B', 'D', 'C', 'B', 'F', 'B', 'A', 'F', 'A', 'A', 'B', 'A', 'C', 'A', 'B', 'C', 'A', 'B', 'B', 'A', 'C', 'A', 'C', 'C', 'A', 'B', 'C', 'F', 'B', 'A', 'C', 'A', 'C', 'B', 'B', 'D', 'A', 'C', 'C', 'B', 'A', 'A', 'B', 'C', 'C', 'A', 'C', 'A', 'A', 'A', 'A', 'C', 'A', 'A', 'B', 'C', 'F', 'B', 'C', 'B', 'B', 'A', 'F', 'A', 'B', 'B', 'C', 'C', 'A', 'A', 'A', 'C', 'D', 'B', 'A', 'C', 'C', 'B', 'A', 'B', 'C', 'B', 'B'], ['F', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'F', 'A', 'F', 'B', 'A', 'F', 'A', 'A', 'B', 'A', 'B', 'A', 'A', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'B', 'C', 'A', 'C', 'D', 'F', 'A', 'A', 'C', 'A', 'D', 'B', 'A', 'C', 'A', 'C', 'C', 'A', 'A', 'A', 'A', 'C', 'B', 'A', 'F', 'A', 'B', 'A', 'A', 'A', 'B', 'A', 'C', 'C', 'C', 'A', 'C', 'B', 'C', 'A', 'B', 'A', 'B', 'B', 'A', 'B', 'B', 'A', 'A', 'C', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'A'])
	('C', 'B')
	"""
	points = {'A':5,'B':4,'C':3,'D':2,'F':1}
	average = {5:'A',4:'B',3:'C',2:'D',1:'F'}
	count_m = 0
	count_f = 0
	for i in  range(len(midterm)):
		count_m += points[midterm[i]]
		count_f += points[final[i]]
	count_m = average[int(count_m/len(midterm))]
	count_f = average[int(count_f/len(final))]
	return count_m, count_f
def average_change(midterm, final):
	"""
	>>> average_change({'A': 29, 'C': 25, 'B': 26, 'D': 3, 'F': 6}, {'A': 43, 'C': 13, 'B': 25, 'D': 2, 'F': 6})
	28
	"""
	points = {'A':2,'B':1,'C':0,'D':-1,'F':-2}
	change = 0
	for i in final:
		change += int((final[i]-midterm[i])*points[i])
	return change
