from django.db import models

# Create your models here.

class Article(models.Model):
	title = models.CharField(max_length=100,null=True,blank=True)
	full_name = models.CharField(max_length=100,null=True,blank=True)
	university = models.CharField(max_length=100,null=True,blank=True)
	affilliation = models.CharField(max_length=100,null=True,blank=True)
	email = models.EmailField(max_length=100,null=True,blank=True)
	phone_no = models.CharField(max_length=100,null=True,blank=True)
	choose_journal = models.CharField(max_length=100,null=True,blank=True)
	article_type = models.CharField(max_length=100,null=True,blank=True)
	article_title = models.CharField(max_length=100,null=True,blank=True)
	attachment_article = models.FileField(upload_to='Article',null=True,blank=True)


class ContactUs(models.Model):
	name= models.CharField(max_length=100,null=True,blank=True)
	email =  models.EmailField(max_length=100,null=True,blank=True)
	phone_no = models.CharField(max_length=100,null=True,blank=True)
	message = models.TextField(max_length=1000,null=True,blank=True)