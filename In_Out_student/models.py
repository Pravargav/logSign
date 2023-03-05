from django.db import models


class Student(models.Model):
    name=models.CharField(max_length=217)
    aadhar_num=models.BigIntegerField(default=0)
    email_id=models.EmailField(max_length=217,default="x")
    mobile_num=models.BigIntegerField(default=0)
    pswrd=models.CharField(max_length=217,default="x")
    




