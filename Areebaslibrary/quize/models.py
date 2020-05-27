from django.db import models

# Create your models here.
from django.db import *
from django.core.validators import MaxValueValidator, MinValueValidator

class Nameoflist(models.Model):
    nameoflist = models.CharField(max_length=150)
    def __str__(self):
        return self.nameoflist



class ListSorting(models.Model):
    number = models.IntegerField(validators=[
            MaxValueValidator(1000000),
            MinValueValidator(0)
        ], blank=False)
    listname =  models.ForeignKey(to=Nameoflist, on_delete=models.CASCADE)
    #def __str__(self):
       # return self.number
class Topic(models.Model):
    topicname= models.CharField(max_length=150)
    def __str__(self):
        return self.topicname

class Blank(models.Model):
    blank= models.CharField(max_length=150)
    blankanswer= models.CharField(max_length=150)
    topic= models.ForeignKey(to=Topic, on_delete=models.CASCADE)
    def __str__(self):
        return self.blank

    '''@property
    def get_special_combination_value(self):
        return '{}{}'.format(self.blank, self.blankanswer)'''


  #  def __str__(self):
   #     return self.number
