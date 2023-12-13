from django.db import models


class Person(models.Model):

    GROUPS=(
        ('A+','A+'),
        ('B+','B+'),
        ('AB+','AB+'),
        ('O+','O+'),
        ('A-','A-'),
        ('B-','B-'),
        ('AB-','AB-'),
        ('O-','O-'),
    )

    image=models.ImageField(upload_to='uploads/images',null=False,blank=False)
    name = models.CharField(max_length=150,null=False,blank=False)
    age = models.IntegerField(null=False,blank=False)
    email=models.EmailField(null=False,blank=False)
    phone=models.CharField(max_length=12,null=False,blank=False)
    place=models.CharField(max_length=100,null=False,blank=False)
    bloodgroup=models.CharField(max_length=3,choices=GROUPS,default='--',null=False,blank=False)

    def __str__(self):
        return self.name
    


