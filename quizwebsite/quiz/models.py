from django.db import models

# Create your models here.

class users(models.Model):
    emailid=models.EmailField()
    firstname=models.CharField(max_length=250)
    lastname=models.CharField(max_length=250)
    password=models.CharField(max_length=250)
    enrollment_no=models.IntegerField()#(max_length=16)
    current_sem=models.IntegerField()
    # department=models.IntegerField()
    is_staff=models.BooleanField(default=False)
    is_student=models.BooleanField(default=False)


    def __str__(self):
        return self.emailid #'%s %s %s'%(self.emailid)#,self.firstname,self.lastname,self.password)
    # def create(self):
    #     self.save()

class subject(models.Model):
    name=models.CharField(max_length=50)
    code=models.IntegerField()
    department=models.CharField(max_length=50)
    semester=models.IntegerField()
    teaching_faculty=models.CharField(max_length=250)
    chapters=models.CharField(max_length=1000)
    
    def __str__(self):
        return self.name
    # def int(self):
    #     return self.code

class question(models.Model):
    exam_code=models.CharField(max_length=100)
    number=models.IntegerField()
    question_type=models.CharField(max_length=100)
    question=models.CharField(max_length=250)
    answer=models.CharField(max_length=250)
    option1=models.CharField(max_length=250)
    option2=models.CharField(max_length=250)
    option3=models.CharField(max_length=250)
    option4=models.CharField(max_length=250)

    def __str__(self):
        return self.question#(self.number,self.question,self.option1,self.option2,self.option3,self.option4,self.answer)

class result(models.Model):
    user_id=models.CharField(max_length=30)
    emailid=models.EmailField()
    examcode=models.CharField(max_length=10)
    submitted_ans=models.CharField(max_length=1000)
    score=models.IntegerField()

    def __str__(self):
        return self.user_id#,self.emailid,self.examcode,self.score)

class quey(models.Model):
    email=models.EmailField()
    name=models.CharField(max_length=200)
    description=models.CharField(max_length=2500)
    timestamp=models.DateField()
    
    def __str__(self):
        return self.emailid
        