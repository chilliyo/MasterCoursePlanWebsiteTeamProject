'''
Qili May 18th
'''
import csv,sys,os

# Full path and name to  csv file (total of 6 csv tables)
is_Classes_csv_filepathname= []

IS_Standard = "/Users/miguelcarrazza/Desktop/MasterCoursePlanWebsiteTeamProject/WebCrawler/IS_Standard.csv"
IS_IT_Enterprise_Management = "/Users/miguelcarrazza/Desktop/MasterCoursePlanWebsiteTeamProject/WebCrawler/IS_IT_Enterprise_Management.csv"
IS_Database_Administration = "/Users/miguelcarrazza/Desktop/MasterCoursePlanWebsiteTeamProject/WebCrawler/IS_Database_Administration.csv"
IS_Business_Systems_Analysis = "/Users/miguelcarrazza/Desktop/MasterCoursePlanWebsiteTeamProject/WebCrawler/IS_Business_Systems_Analysis.csv"
IS_Business_Intelligence = "/Users/miguelcarrazza/Desktop/MasterCoursePlanWebsiteTeamProject/WebCrawler/IS_Business_Intelligence.csv"

is_Classes_csv_filepathname.append(IS_Standard)
is_Classes_csv_filepathname.append(IS_IT_Enterprise_Management)
is_Classes_csv_filepathname.append(IS_Database_Administration)
is_Classes_csv_filepathname.append(IS_Business_Systems_Analysis)
is_Classes_csv_filepathname.append(IS_Business_Intelligence)

CS = "/Users/miguelcarrazza/Desktop/MasterCoursePlanWebsiteTeamProject/WebCrawler/DePaul_Master_ComputerScience_Standard_manuallyAddClassType.csv"
# Full path to django project directory
djangoproject_home="/Users/miguelcarrazza/Desktop/MasterCoursePlanWebsiteTeamProject/src"

sys.path.append(djangoproject_home)

os.environ['DJANGO_SETTINGS_MODULE'] = 'MySite.settings'

import django

django.setup()

from MyHome.models import is_Classes
from MyHome.models import cs_Classes

for csv_file in is_Classes_csv_filepathname:
	data = csv.reader(open(csv_file), delimiter=',', quotechar='"')
	for row in data:
		if row[0] != 'COURSE_NUMBER':
			# Ignore the header row, import everything else
			isclasses = is_Classes()
			isclasses.class_number = row[0]
			isclasses.class_name = row[1]
			isclasses.pre_req = row[2]
			isclasses.class_type = row[3]
			isclasses.fall = row[4]
			isclasses.winter = row[5]
			isclasses.spring = row[6]
			isclasses.summer = row[7]
			isclasses.online = row[8]
			isclasses.save()
data = csv.reader(open(CS, 'rU'), delimiter=',', quotechar='"',dialect=csv.excel_tab)
#data = csv.reader(open(CS), delimiter=',', quotechar='"')
for row in data:
	if row[0] != 'COURSE_NUMBER':
		# Ignore the header row, import everything else
		csclasses = cs_Classes()
		csclasses.class_number = row[0]
		csclasses.class_name = row[1]
		csclasses.pre_req = row[2]
		csclasses.class_type = row[3]
		csclasses.fall = row[4]
		csclasses.winter = row[5]
		csclasses.spring = row[6]
		csclasses.summer = row[7]
		csclasses.online = row[8]
		csclasses.save()
