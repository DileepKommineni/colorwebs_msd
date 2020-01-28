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

class Publication(models.Model):
	publication_name = models.TextField(max_length=1000,null=True,blank=True)

	def __str__(self):
		return self.publication_name

class PublicationImages(models.Model):
	publication = models.ForeignKey(
								Publication, 
								on_delete=models.CASCADE,
								null=True,
								blank=True,
								)
	publication_image =  models.ImageField(
								upload_to ='publication_images',
								default='default.jpg',
								)

	def __str__(self):
		return self.publication_name

class EditorialBoard(models.Model):
	publication = models.ForeignKey(
								Publication, 
								on_delete=models.CASCADE,
								null=True,
								blank=True,
								)
	role = models.CharField(max_length=100,null=True,blank=True)
	name = models.CharField(max_length=100,null=True,blank=True)
	designation = models.CharField(max_length=100,null=True,blank=True)
	department = models.CharField(max_length=100,null=True,blank=True)
	email = models.CharField(max_length=100,null=True,blank=True)
	university = models.CharField(max_length=100,null=True,blank=True)
	country = models.CharField(max_length=100,null=True,blank=True)
	biography = models.TextField(max_length=1000,null=True,blank=True)
	image =  models.ImageField(
								upload_to ='editor_images',
								default='default.jpg',
								)

	def __str__(self):
		return self.name


class CurrentIssues(models.Model):
	issue_no = models.CharField(max_length=100,null=True,blank=True)
	issue_name = models.CharField(max_length=100,null=True,blank=True)
	intro = models.TextField(max_length=1000,null=True,blank=True)
	full_text = models.TextField(max_length=1000,null=True,blank=True)
	artical_type = models.CharField(max_length=100,null=True,blank=True)
	issues_pdf = models.FileField(
								upload_to ='current_issues',
								default='default.jpg',
								)

class Archive(models.Model):
	issue_no = models.CharField(max_length=100,null=True,blank=True)
	issue_name = models.CharField(max_length=100,null=True,blank=True)
	intro = models.TextField(max_length=1000,null=True,blank=True)
	full_text = models.TextField(max_length=1000,null=True,blank=True)
	artical_type = models.CharField(max_length=100,null=True,blank=True)
	issues_pdf = models.FileField(
								upload_to ='archive',
								default='default.jpg',
								)

