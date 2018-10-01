import unittest

from database_test import CS_Class

class TestClassWrapper(unittest.TestCase):
	def test_read_file(self):
		"""
		This def's only function is reading the file it was given and returns the data contents in the file.
		"""
		c = CS_Class()
		data = c.read_file('grade-data.json')
		self.assertEqual(data, [[u'F2008', u'M', u'F', u'F'], [u'F2013', u'M', u'C', u'B'], [u'F2013', u'F', u'A', u'A'], [u'F2013', u'M', u'B', u'A'], [u'S2018', u'M', u'B', u'B'], [u'F2013', u'F', u'C', u'A'], [u'F2012', u'M', u'B', u'A'], [u'F2008', u'M', u'D', u'B'], [u'S2010', u'M', u'C', u'F'], [u'S2011', u'M', u'B', u'A'], [u'F2013', u'M', u'F', u'F'], [u'F2014', u'M', u'B', u'B'], [u'F2014', u'M', u'A', u'A'], [u'S2016', u'M', u'F', u'F'], [u'F2012', u'F', u'A', u'A'], [u'F2012', u'F', u'A', u'A'], [u'S2016', u'F', u'B', u'B'], [u'S2016', u'M', u'A', u'A'], [u'S2010', u'F', u'C', u'B'], [u'F2013', u'F', u'A', u'A'], [u'F2008', u'M', u'B', u'A'], [u'F2011', u'M', u'C', u'A'], [u'S2016', u'M', u'A', u'A'], [u'F2017', u'M', u'B', u'B'], [u'S2018', u'M', u'B', u'B'], [u'F2015', u'M', u'A', u'A'], [u'F2013', u'M', u'C', u'B'], [u'S2011', u'M', u'A', u'A'], [u'F2009', u'M', u'C', u'B'], [u'F2010', u'M', u'C', u'C'], [u'F2012', u'M', u'A', u'A'], [u'F2012', u'M', u'B', u'C'], [u'F2013', u'M', u'C', u'D'], [u'F2013', u'M', u'F', u'F'], [u'F2013', u'M', u'B', u'A'], [u'F2009', u'M', u'A', u'A'], [u'F2014', u'M', u'C', u'C'], [u'S2012', u'M', u'A', u'A'], [u'F2015', u'M', u'C', u'D'], [u'S2014', u'M', u'B', u'B'], [u'S2011', u'M', u'B', u'A'], [u'F2008', u'M', u'D', u'C'], [u'S2012', u'F', u'A', u'A'], [u'S2016', u'M', u'C', u'C'], [u'F2015', u'M', u'C', u'C'], [u'F2013', u'M', u'B', u'A'], [u'F2013', u'F', u'A', u'A'], [u'S2015', u'M', u'A', u'A'], [u'F2009', u'F', u'B', u'A'], [u'S2016', u'M', u'C', u'C'], [u'F2008', u'M', u'C', u'B'], [u'F2015', u'M', u'A', u'A'], [u'S2018', u'M', u'C', u'F'], [u'F2008', u'M', u'A', u'A'], [u'S2018', u'M', u'A', u'B'], [u'S2014', u'M', u'A', u'A'], [u'S2014', u'M', u'A', u'A'], [u'F2008', u'M', u'C', u'A'], [u'S2014', u'M', u'A', u'B'], [u'F2011', u'F', u'A', u'A'], [u'F2015', u'M', u'B', u'C'], [u'F2013', u'M', u'C', u'C'], [u'F2012', u'M', u'F', u'C'], [u'F2014', u'M', u'B', u'A'], [u'F2015', u'M', u'C', u'C'], [u'S2016', u'M', u'B', u'B'], [u'F2014', u'M', u'B', u'C'], [u'F2012', u'M', u'A', u'A'], [u'F2010', u'M', u'F', u'B'], [u'S2012', u'M', u'A', u'A'], [u'S2017', u'M', u'B', u'B'], [u'S2015', u'M', u'B', u'B'], [u'S2009', u'M', u'C', u'A'], [u'F2008', u'M', u'C', u'B'], [u'S2014', u'M', u'A', u'B'], [u'F2013', u'F', u'A', u'A'], [u'S2016', u'M', u'A', u'A'], [u'F2015', u'M', u'C', u'C'], [u'S2014', u'F', u'D', u'B'], [u'F2009', u'M', u'B', u'A'], [u'F2010', u'M', u'A', u'A'], [u'S2009', u'F', u'C', u'B'], [u'F2015', u'F', u'C', u'B'], [u'S2010', u'M', u'B', u'A'], [u'S2014', u'M', u'A', u'A'], [u'S2010', u'F', u'B', u'B'], [u'F2008', u'M', u'C', u'B'], [u'F2008', u'F', u'B', u'A'], [u'F2009', u'M', u'B', u'A']])
	def test_count_male(self):
		"""
		The only function of this function is to count all the male students in the data.
		"""
		c = CS_Class()
		data = c.read_file('grade-data.json')
		m = c.count_male(data)
		self.assertEqual(m, 72)
	def test_count_female(self):
		"""
		The only function of this function is to count all the female students in the data.
		"""
		c = CS_Class()
		data = c.read_file('grade-data.json')
		f = c.count_female(data)
		self.assertEqual(f,17)
	def test_grades_m(self):
		"""
		Find all the midterm grades of every student in the data file.
		"""
		c = CS_Class()
		data = c.read_file('grade-data.json')
		m = c.grades_m(data)
		self.assertEqual(m,['F', 'C', 'A', 'B', 'B', 'C', 'B', 'D', 'C', 'B', 'F', 'B', 'A', 'F', 'A', 'A', 'B', 'A', 'C', 'A', 'B', 'C', 'A', 'B', 'B', 'A', 'C', 'A', 'C', 'C', 'A', 'B', 'C', 'F', 'B', 'A', 'C', 'A', 'C', 'B', 'B', 'D', 'A', 'C', 'C', 'B', 'A', 'A', 'B', 'C', 'C', 'A', 'C', 'A', 'A', 'A', 'A', 'C', 'A', 'A', 'B', 'C', 'F', 'B', 'C', 'B', 'B', 'A', 'F', 'A', 'B', 'B', 'C', 'C', 'A', 'A', 'A', 'C', 'D', 'B', 'A', 'C', 'C', 'B', 'A', 'B', 'C', 'B', 'B'])
	def test_grades_f(self):
		"""
		Find all the final grades of every student in the data file.
		"""
		c = CS_Class()
		data = c.read_file('grade-data.json')
		f = c.grades_f(data)
		self.assertEqual(f,['F', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'F', 'A', 'F', 'B', 'A', 'F', 'A', 'A', 'B', 'A', 'B', 'A', 'A', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'B', 'C', 'A', 'C', 'D', 'F', 'A', 'A', 'C', 'A', 'D', 'B', 'A', 'C', 'A', 'C', 'C', 'A', 'A', 'A', 'A', 'C', 'B', 'A', 'F', 'A', 'B', 'A', 'A', 'A', 'B', 'A', 'C', 'C', 'C', 'A', 'C', 'B', 'C', 'A', 'B', 'A', 'B', 'B', 'A', 'B', 'B', 'A', 'A', 'C', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'A'])
	def test_grades_count_m(self):
		"""
		Count all the midterm letter grades in the file, have a counter for A,B,C,D,F.
		"""
		c = CS_Class()
		data = c.read_file('grade-data.json')
		m1 = c.grades_m(data)
		m = c.grades_count_m(m1)
		self.assertEqual(m,{'A': 29, 'C': 25, 'B': 26, 'D': 3, 'F': 6})
	def test_grades_count_f(self):
		"""
		Count all the final letter grades in the file, have a counter for A,B,C,D,F.
		"""
		c = CS_Class()
		data = c.read_file('grade-data.json')
		f1 = c.grades_f(data)
		f = c.grades_count_f(f1)
		self.assertEqual(f,{'A': 43, 'C': 13, 'B': 25, 'D': 2, 'F': 6})
	def test_grade_avg_m(self):
		"""
		Calculate the average letter grade of the class based on the midterm letter grades of the students in the data file.
		"""
		c = CS_Class()
		data = c.read_file('grade-data.json')
		m1 = c.grades_m(data)
		m = c.grade_avg_m(m1)
		self.assertEqual(m,"C")
	def test_grade_avg_f(self):
		"""
		Calculate the average letter grade of the class based on the final letter grades of the students in the data file.
		"""
		c = CS_Class()
		data = c.read_file('grade-data.json')
		f1 = c.grades_f(data)
		f = c.grade_avg_f(f1)
		self.assertEqual(f,"B")
	def test_average_change(self):
		"""
		Find the average letter grade change in the class overall. Did the class's overall students improve or worsen? And by how much?
		"""
		c = CS_Class()
		data = c.read_file('grade-data.json')
		m2 = c.grades_m(data)
		m1 = c.grades_count_m(m2)
		f2 = c.grades_f(data)
		f1 = c.grades_count_f(f2)
		result = c.average_change(m1, f1)
		self.assertEqual(result,28)
if __name__ == '__main__':
	unittest.main()
