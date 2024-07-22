from django.db import models



# Create your models here.
#class description
class Description (models.Model):
    descript=models.TextField(blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.Description

    #course
class Course(models.Model): 
    name=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)  
    Description=models.OneToOneField(Description,on_delete=models.CASCADE) #link
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

#######################

def create_description(descript):
    return Description.descript.objects.create(descript=descript)


#all objects of Description
def getalldescription():
    return Description.objects.all()
########################

def addcourse(name,Description):
        course = Course.objects.create(name= name,Description=Description)
        
        return course



#comment
class Comment (models.Model):
    comment=models.TextField(blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    course=models.ForeignKey(Course,related_name='Comments',on_delete=models.CASCADE) #link
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Comment
####
def comment_to_course(comment):
    return Course.objects.create(comment=comment)

#methods: 


##all Objects of Course##
def getallcourse():
    return Course.objects.all()
##need to add Course

#all objects of comment
def getallcomment():
    return Comment.objects.all()


