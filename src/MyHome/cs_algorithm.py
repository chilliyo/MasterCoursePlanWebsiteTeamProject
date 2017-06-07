from .models import cs_Classes
import re





class Contents:
    classes_taken = ["None",'']
    intro_classes = ["CSC400","CSC401", "CSC402","CSC403","CSC406", "CSC407"]
    foundation_classes = ["CSC421","CSC435","CSC447","CSC453"]

    def __init__():
        self.classes_taken = ["None",'']
        self.intro_classes = ["CSC400","CSC401", "CSC402","CSC403","CSC406", "CSC407"]
        self.foundation_classes = ["CSC421","CSC435","CSC447","CSC453"]

is_class_reqs = [0,4,0,8,1]

student = Contents

def quarter_classes(quarter, classType):
    if quarter == "Fall":
        candidates = cs_Classes.objects.filter(class_type= classType, fall = True)
    elif quarter == "Summer":
        candidates = cs_Classes.objects.filter(class_type= classType, summer = True)
    elif quarter == "Winter":
        candidates = cs_Classes.objects.filter(class_type= classType, winter = True)
    else:
        candidates = cs_Classes.objects.filter(class_type= classType, spring = True)

    return candidates


def get_class(classType, schedule, maxx, classes_taken, quarter, online, summer):
    candidates = quarter_classes(quarter, classType)
    for clazz in candidates:
        if((clazz.class_number not in classes_taken) and check_reqs(clazz.pre_req, classes_taken)):
            classes_taken.append(clazz.class_number)
            return clazz.class_number


def get_class_reqs(reqs):
    reqs_list = []
    reqs = re.sub('[\(\)\{\}<>]', "", reqs)
    reqs_list = reqs.split("and")
    for i in range(0, reqs_list.__len__()):
        reqs_list[i] = remove_spaces(reqs_list[i])
        if "or" in reqs_list[i]:
            reqs_list[i] = reqs_list[i].split("or")
        #reqs_list[i] = remove_spaces(reqs_list[i])
    return(reqs_list)


def check_reqs(reqs, classes_taken):
    reqs = get_class_reqs(reqs)
    for i in range(0, len(reqs)):
        if type(reqs[i]) == list:
            if any(req in classes_taken for req in reqs[i]) == False:
                return False
        else:
            if reqs[i] not in classes_taken:
                return False
        #print(req)
    return True

def remove_spaces(string):
    newstring = ''
    for i in string:
        if i != " ":
            newstring = newstring+i
    return newstring

def get_maxx(class_arg):
    for i in class_arg:
        if i.isdigit():
            return int(i)


def check_completion(list1, list2):
    for i in list1:
        if i not in list2:
            return False
    return True



def single_quarter_classes(profile, quarter):
    schedule = []
    maxx = get_maxx(profile.Classes_Per_Quarter)

    i = 1

    for j in range(0,maxx):
        if check_completion(student.intro_classes, student.classes_taken) == False:
            clazz = get_class("1", schedule, maxx, student.classes_taken, quarter, profile.online, profile.summer)
            schedule.append(clazz)
            #classes_taken.append(clazz)
        elif check_completion(student.foundation_classes, student.classes_taken) == False:
            clazz = get_class("2", schedule, maxx, student.classes_taken, quarter, profile.online, profile.summer)
            schedule.append(clazz)
            #classes_taken.append(clazz)
        else:
            clazz = get_class("3", schedule, maxx, student.classes_taken, quarter, profile.online, profile.summer)
            schedule.append(clazz)
            #classes_taken.append(clazz)


    return schedule



def cs_get_path(profile):
    maxx = get_maxx(profile.Classes_Per_Quarter)
    if profile.summer:
        quarters = ["Fall", "Winter", "Spring", "Summer"]
    else:
        quarters = ["Fall", "Winter", "Spring"]
    path = []
    classes = 0
    i = 0

    while classes <= 16:
        if i == (len(quarters) - 1):
            path.append(single_quarter_classes(profile, quarters[i]))
            classes = classes + maxx
            i = 0
        else:
            path.append(single_quarter_classes(profile, quarters[i]))
            classes = classes + maxx
            i = i + 1

    student.classes_taken = ["None", ""]
    return path
