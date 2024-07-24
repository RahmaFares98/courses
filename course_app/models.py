from django.db import models

# Create your models here.


class CourseManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['name']) < 5:
            errors["name"] = "Course Name should be at least 10 characters"
        if len(postData['description']) < 15:
            errors["description"] = "Description  should be at least 15 characters"
        return errors

#class description
class Description (models.Model):
    descript=models.TextField(blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.descript

    #course
class Course(models.Model): 
    name=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)  
    Description=models.OneToOneField(Description,on_delete=models.CASCADE) #link
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()    # add this line!

    #Comments
    def __str__(self):
        return self.name

#######################

def create_description(CourseDescript):
    CourseDescript= Description.objects.create(descript=CourseDescript)
    print(CourseDescript)
    return CourseDescript


#all objects of Description
def getalldescription():
    return Description.objects.all()
########################

def addcourse(name,Description):
        course = Course.objects.create(name= name,Description=Description)
        return course




def create_comment(comment,course):
    Comment.objects.create(comment=comment,course=course)
    
#comment
class Comment (models.Model):
    comment=models.TextField(blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    course=models.ForeignKey(Course,related_name='Comments',on_delete=models.CASCADE) #link
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment
####
#methods: 


##all Objects of Course##
def getallcourse():
    return Course.objects.all()
##need to add Course

#all objects of comment
def getallcomment():
    return Comment.objects.all()

def get_data_course(id):
    return Course.objects.get(id=id)


