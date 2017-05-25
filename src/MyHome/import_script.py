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

from MyHome.models import cs_Classes

for csv_file in csv_filepathname:
	data = csv.reader(open(csv_file), delimiter=',', quotechar='"') 
		for row in data:
			if row[0] != 'COURSE_NUMBER':
			# Ignore the header row, import everything else
				cs_Classes = cs_Classes()
				cs_Classes.class_number = row[0]
				cs_Classes.class_name = row[1]
				cs_Classes.pre_req = row[2]
				cs_Classes.class_type = row[3]
				cs_Classes.fall = row[4]
				cs_Classes.winter = row[5]
				cs_Classes.spring = row[6]
				cs_Classes.summer = row[7]
				cs_Classes.online = row[8]
				cs_Classes.save()


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