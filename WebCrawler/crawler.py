'''
Author: Qili Sui
Master Course Plan Website Team Project
'''
import csv
import urllib
from bs4 import BeautifulSoup
import pandas as pd
import re
import string

PREFIX = 'http://www.cdm.depaul.edu/academics/pages/courseinfo.aspx?'
SUBJECT = ''
COURSE_NUMBER = ''

def get_class(url = "http://www.cdm.depaul.edu/academics/Pages/Current/Requirements-MS-in-Computer-Science.aspx"):
    global SUBJECT
    global COURSE_NUMBER
    COURSE_URL = ''
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html, "lxml")

    #print html

    #class_name = re.compile("CDMExtendedCourseInfo...*")

    courseCode_html = soup.findAll('td', {'class': "CDMExtendedCourseInfo"})

    courseCode = []
    courseURLs = []
    for course in courseCode_html:
        courseCode.append(course.text)

    for course in courseCode_html:
        course_code_split = course.text.split()
        SUBJECT = course_code_split[0]
        COURSE_NUMBER = course_code_split[1]
        COURSE_URL  = PREFIX + 'Subject=' + SUBJECT + '&CatalogNbr='+ COURSE_NUMBER
        courseURLs.append(COURSE_URL)

    return courseURLs

def get_course_detail_page(courseURLs):
    #regex = re.compile('<div>...*PREREQUISITE...*</div>')
    stripped_course_rows = []
    for url in courseURLs:
        print("Getting Course Infomation from " + url + " ...")
        html = urllib.urlopen(url).read()
        soup = BeautifulSoup(html, "lxml")
        course_Page_title = soup.find('h2',{'class':'CDMPageTitle'})
        try:
            course_row = course_Page_title.text.strip('\r\n ').split(':')
        except:
            pass

        #get PREREQUISITE
        PREREQUISITE = soup.find(id='ctl00_ctl63_g_50f24079_ef2e_419b_a791_15cbeadc76ee').contents

        if 'PREREQUISITE(S):' in PREREQUISITE[3].text:
            PREREQUISITE_classes = (PREREQUISITE[3].text.split(":")[1].strip(": "))
        else:
            PREREQUISITE_classes = None
        if 'Prerequisites:' in PREREQUISITE[3].text:
            PREREQUISITE_classes = (PREREQUISITE[3].text.split(":")[1].strip(": "))
        if 'PREREQUISITE(S)' in PREREQUISITE[3].text:
            PREREQUISITE_classes = (PREREQUISITE[3].text.split("PREREQUISITE(S)")[1].strip(": "))

        #check if the class was offered in summer session
        if_offers_summer = 0
        offered_quarters = soup.findAll('p', {'class':'CTIPageSectionHeader'})
        for quarter in offered_quarters:
            #print quarter.text[0:5]
            #print (quarter.text[0:5] == 'Summe')
            if quarter.text[0:6] == 'Summer':
                if_offers_summer = 1
                break
                #print if_offers_summer

        #check if the class was offered online
        class_location_list = []
        if_offers_online = 0
        class_info = soup.findAll('div', {'class': 'classInfo'})
        for info in class_info:
            children = info.findChildren()
            try:
                class_location_list.append(children[3].text)
            except:
                pass

        for location in class_location_list:
            if location[-13:-1] == 'Online Campu':
                if_offers_online = 1
                break


        #cleaning the data
        stripped_course_row = []
        for item in course_row:
            stripped_item = re.sub('\r\n\    ', '', item)
            stripped_course_row.append(stripped_item)

        stripped_course_row.append(PREREQUISITE_classes)
        stripped_course_row.append('N/A')
        stripped_course_row.append(if_offers_summer)
        stripped_course_row.append(if_offers_online)
        print stripped_course_row
        stripped_course_rows.append(stripped_course_row)
    return stripped_course_rows


def write_table(course_row):
    print("Writing Data to csv table...")
    colums = ['COURSE_NUMBER','COURSE_NAME','PREREQUISITE','CLASS_TYPE', 'SUMMER', 'ONLINE']
    with open('DePaul_Master_ComputerScience_Standard.csv', 'w') as myfile:
        writer = csv.writer(myfile)
        writer.writerow(colums)
        for row in course_row:
            writer.writerow(row)

    print("CSV file are ready.")
#write_table(get_class())
write_table(get_course_detail_page(get_class()))
#get_course_detail_page(get_class())