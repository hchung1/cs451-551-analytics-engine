import json
#unittest
def read_file():
  with open('grade-data.json') as f:
    data = json.loads(f.read())
  return data
def gender(data):
  males=0
  females = 0
  for i in range(len(data)):
    if (data[i][1]=='M'):
      males += 1
    if (data[i][1]=='F'):
      females += 1
  print ("There are %i females in the database.\n" % (females))
  print ("There are %i males in the database.\n\n" % (males))
  return males, females
def grades(data):
  midterm = []
  final = []
  for i in range(len(data)):
    midterm.append(str(data[i][2]))
    final.append(str(data[i][3]))
  print ("This is the midterm list: %s.\n" % (str(midterm)))
  print ("This is the final list: %s.\n\n" % (str(final)))
  return midterm, final
def grades_count(mid, final):
  counter_mid = {'A':0,'B':0,'C':0,'D':0,'F':0}
  counter_final = {'A':0,'B':0,'C':0,'D':0,'F':0}
  for i in range(len(mid)):
    counter_mid[mid[i]] += 1
    counter_final[final[i]] += 1
  print ("This is the midterm grade count: %s.\n" % (str(counter_mid)))
  print ("This is the final grade count: %s.\n\n" % (str(counter_final)))
  return counter_mid, counter_final
def grade_avg(midterm, final):
  points = {'A':5,'B':4,'C':3,'D':2,'F':1}
  average = {5:'A',4:'B',3:'C',2:'D',1:'F'}
  count_m = 0
  count_f = 0
  for i in  range(len(midterm)):
    count_m += points[midterm[i]]
    count_f += points[final[i]]
  count_m = average[int(count_m/len(midterm))]
  count_f = average[int(count_f/len(final))]
  print ("The average class grade for final is %s.\n\n" % (count_f))
  return count_m, count_f
def average_change(midterm, final):
  points = {'A':2,'B':1,'C':0,'D':-1,'F':-2}
  change = 0
  for i in final:
    change += int((final[i]-midterm[i])*points[i])
  hi = "remained the same"
  if (change > 0):
    hi = "increased"
  if (change < 0):
    hi = "decreased"
  print ("The overall grade average change in class %s by %i points.\n" % (hi, change))
data = read_file()
males, females = gender(data)
midterm, final = grades(data)
counter_mid, counter_final = grades_count(midterm, final)
avg_m, avg_f = grade_avg(midterm, final)
change = average_change(counter_mid, counter_final)
