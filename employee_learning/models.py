from django.db import models
import datetime
# Create your models here.
class Division(models.Model):
    div_name=models.CharField(max_length=25)
    fuck_you=models.BooleanField (help_text="If you want to get fucked,please click this")
    fuck_me=models.DateTimeField(help_text="If you want to get fucked,please click this",verbose_name='时间')
    List=[('高','High'),('中','Medium'),('低','Low')]
    fuck_them=models.ImageField(verbose_name='请上传你的证件照')
    priority=models.CharField(max_length=1,choices=List,default='高',verbose_name='优先级')
    def __str__(self):
        return self.div_name
    
class Employees(models.Model):
    name = models.CharField(max_length=25)
    division = models.ForeignKey(Division,on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class PersonalInfo(models.Model):
    name=models.OneToOneField(Employees,on_delete=models.CASCADE,primary_key=True)   ##一对一
    tel=models.CharField(max_length=15)
    address=models.CharField(max_length=50)
    def __str__(self):
        return self.name.name

class LearningCourse (models.Model):
    LEVEL=[('B','Basic'),('I','Intermediate'),('A','Advanced'),]
    title = models.CharField(max_length=50,unique=True)
    level = models.CharField(max_length=1,choices=LEVEL,default="I")
    employee = models.ManyToManyField(Employees)                ##多对多
    def __str__ (self):
        return self.title
