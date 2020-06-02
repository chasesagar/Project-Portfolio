from django.db import models

# Create your models here.

class home(models.Model):
    
    name = models.CharField(max_length=12)
    
    desc = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pictures')

class socialconnect(models.Model):

    facebook = models.CharField(max_length=100)
    instagram = models.CharField(max_length=100)
    twitter = models.CharField(max_length=100)
    linkedin = models.CharField(max_length=100)
    website = models.CharField(max_length=100)

class sidenavbar(models.Model):

    row_1 = models.CharField(max_length=11)
    row_2 = models.CharField(max_length=11)
    row_3 = models.CharField(max_length=11)
    row_4 = models.CharField(max_length=11)
    row_5 = models.CharField(max_length=11)
    row_6 = models.CharField(max_length=11)
    
class about(models.Model):
    title = models.CharField(max_length=50)
    desc = models.TextField()

class education(models.Model):

    img = models.ImageField('pictures')
    title = models.CharField(max_length=50)
    sub_title = models.CharField(max_length=100)

class skills(models.Model):

    img = models.ImageField('pictures')
    title = models.CharField(max_length=50)
    sub_title = models.CharField(max_length=100)

class certificate(models.Model):

    img = models.ImageField('pictures')
    title = models.CharField(max_length=100)

class solution(models.Model):

    title = models.TextField()

    one = models.CharField(max_length=100)
    one_title = models.TextField()

    two = models.CharField(max_length=100)
    two_title = models.TextField()

    three = models.CharField(max_length=100)
    three_title = models.TextField()

    four = models.CharField(max_length=100)
    four_title = models.TextField()

    five = models.CharField(max_length=100)
    five_title = models.TextField()

    six = models.CharField(max_length=100)
    six_title = models.TextField()

class project(models.Model):

    title = models.CharField(max_length=100)
    img = models.ImageField('pictures')
    description = models.TextField()
    link = models.CharField(max_length=200)
    extra = models.TextField()   

class contact(models.Model):

    title = models.CharField(max_length=300)
    mobile1 = models.CharField(max_length=15)
    mobile2 = models.CharField(max_length=15)
    email = models.CharField(max_length=100)
    address_line_1 = models.CharField(max_length=100)
    address_line_2 = models.CharField(max_length=100)
    link = models.CharField(max_length=200)
    extra = models.TextField() 

class subscribe(models.Model):

    title = models.CharField(max_length=150)
    description = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)