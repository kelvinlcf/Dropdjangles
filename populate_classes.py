#usr/bin/python

#sys path
import re
import sys
sys.path.insert(0, '/dropjangles/')

#env variabls
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dropjangles.settings')

#mdels
from timetable.models import Course, Class

#django functions
import django
django.setup()

def populate():
    #populate courses
    courseFile = open("courseLIST.txt")
    i = 0
    for course in courseFile.readlines():
        break
        course = course.strip()
        #print course
        exec(course)
        #course.save()
        i = i + 1

    #populate classes
    #classFile = open("classLIST.txt")
    classFile = open("django_class_list_with_streams.txt")
    #classFile = open("test_stream.txt")

    #initialise stream slots (currently max of 9)
    class1 = None
    class2 = None
    class3 = None
    class4 = None
    class5 = None
    class6 = None
    class7 = None
    class8 = None
    class9 = None
    c1 = None
    c2 = None
    c3 = None
    c4 = None
    c5 = None
    c6 = None
    c7 = None
    c8 = None
    c9 = None
    stream_list = []

    for clss in classFile.readlines():
        #get current class
        clss = clss.strip()
#        break
#        sys.stdout.write("    CURRENT LINE --> {0}\n".format(clss))
        if ('next-stream' in clss):
            sys.stdout.write("    STREAM LIST --> {0}\n\n".format(stream_list))           
            for currClass in stream_list:
                for currClass2 in stream_list:
                    if (currClass != currClass2):
                        print("    {0}:{1} --> {2}:{3}\n".format(currClass.name, currClass.id, currClass2.name, currClass2.id))
                        currClass.shared_stream.add(currClass2)
                        currClass2.shared_stream.add(currClass)
                        currClass.save()
                        currClass2.save()

            #start linking everything
            #reset c1,c2...c6
            class1 = None
            class2 = None
            class3 = None
            class4 = None
            class5 = None
            class6 = None
            class7 = None
            class8 = None
            class9 = None
            c1 = None
            c2 = None
            c3 = None
            c4 = None
            c5 = None
            c6 = None
            c7 = None
            c8 = None
            c9 = None
            stream_list = []

        currCrs = clss
        crsFind = re.search(r'([A-Z]{4}[0-9]{4})',currCrs)        
        if (crsFind is not None):
            currCrs = crsFind.group(1)
            relatedCourse = Course.objects.get(name=currCrs)
            sys.stdout.write("    RELATED COURSE --> {0}\n".format(relatedCourse))
            exec(clss)
 
            if c1 is not None:
                c1.course_id = relatedCourse.id                
                c1.save()

                for clsss in Class.objects.raw("SELECT * FROM timetable_class WHERE timetable_class.id={0}".format(c1.id)):
                    class1=clsss
                    stream_list.append(class1)
                    break

            if c2 is not None:
                c2.course_id = relatedCourse.id
                c2.save()

                for clsss in Class.objects.raw("SELECT * FROM timetable_class WHERE timetable_class.id={0}".format(c2.id)):
                    class2=clsss
                    stream_list.append(class2)
                    break

            if c3 is not None:
                c3.course_id = relatedCourse.id
                c3.save()

                for clsss in Class.objects.raw("SELECT * FROM timetable_class WHERE timetable_class.id={0}".format(c3.id)):
                    class3=clsss
                    stream_list.append(class3)
                    break

            if c4 is not None:
                c4.course_id = relatedCourse.id
                c4.save()

                for clsss in Class.objects.raw("SELECT * FROM timetable_class WHERE timetable_class.id={0}".format(c4.id)):
                    class4=clsss
                    stream_list.append(class4)
                    break

            if c5 is not None:
                c5.course_id = relatedCourse.id
                c5.save()

                for clsss in Class.objects.raw("SELECT * FROM timetable_class WHERE timetable_class.id={0}".format(c5.id)):
                    class5=clsss
                    stream_list.append(class5)
                    break

            if c6 is not None:
                c6.course_id = relatedCourse.id
                c6.save()

                for clsss in Class.objects.raw("SELECT * FROM timetable_class WHERE timetable_class.id={0}".format(c6.id)):
                    class6=clsss
                    stream_list.append(class6)
                    break

            if c7 is not None:
                c7.course_id = relatedCourse.id
                c7.save()

                for clsss in Class.objects.raw("SELECT * FROM timetable_class WHERE timetable_class.id={0}".format(c7.id)):
                    class7=clsss
                    stream_list.append(class7)
                    break

            if c8 is not None:
                c8.course_id = relatedCourse.id
                c8.save()

                for clsss in Class.objects.raw("SELECT * FROM timetable_class WHERE timetable_class.id={0}".format(c8.id)):
                    class8=clsss
                    stream_list.append(class8)
                    break

            if c9 is not None:
                c9.course_id = relatedCourse.id
                c9.save()

                for clsss in Class.objects.raw("SELECT * FROM timetable_class WHERE timetable_class.id={0}".format(c9.id)):
                    class9=clsss
                    stream_list.append(class9)
                    break

#start population
if __name__ == '__main__':
    print "Starting timetable population from scraper"
    populate()

# ADD COURSE
# CHAR NAME, INT YEAR, INT SEMESTER

# ADD CLASS
# CHAR NAME, INT timeFrom, INT timeTo, INT classtype, INT day, INT course_id
