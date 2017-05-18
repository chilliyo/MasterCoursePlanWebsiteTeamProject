'''
Qili May 18th
'''
import csv,sys,os 

# Full path and name to  csv file (total of 6 csv tables)
csv_filepathname= ["path","path","path","path","path","path"] 

# Full path to django project directory 
djangoproject_home=""

sys.path.append(djangoproject_home)

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django

django.setup()

from MyHome.models import Classes

for csv_file in csv_filepathname:
	data = csv.reader(open(csv_file), delimiter=',', quotechar='"') 
		for row in data:
			if row[0] != 'COURSE_NUMBER':
			# Ignore the header row, import everything else
				classes = Classes()
				classes.class_number = row[0]
				classes.class_name = row[1]
				classes.pre_req = row[2]
				classes.class_type = row[3]
				classes.fall = row[4]
				classes.winter = row[5]
				classes.spring = row[6]
				classes.summer = row[7]
				classes.online = row[8]
				zipcode.save()


'''
COURSE_NUMBER,COURSE_NAME,PREREQUISITE,CLASS_TYPE,FALL,WINTER,SPRING,SUMMER,ONLINE
CSC400,Discrete Structures for Computer Science,,N/A,1,1,1,1,1
CSC401,Introduction to Programming,None,N/A,1,1,1,1,1
CSC402,Data Structures I,CSC 401,N/A,1,1,1,1,1
CSC403,Data Structures II,CSC 402,N/A,1,1,1,1,1
CSC406,Systems I,CSC 401,N/A,1,1,1,1,1
CSC407,Systems II,CSC 406 and CSC 402,N/A,1,1,1,1,1
...etc.
'''