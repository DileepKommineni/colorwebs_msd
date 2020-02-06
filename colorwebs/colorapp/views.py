from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from colorapp.models import (
								Article,
								ContactUs,
								Publication,
								EditorialBoard,
								CurrentIssues,
								Archive,

							)

# Create your views here.

def home(request):
	return render(request,'static/index.html')

def signup_user(request):
	return render(request,'static/signup.html')

def signup_submit(request):
	if (request.POST.get("password") == request.POST.get("cnf-password")):
		try:
			User.objects.get(username=request.POST.get("username"))
			messages.error(request, 'Username exits')
			return render(request,'static/signup.html')
		except:
			User.objects.create(
							username = request.POST.get("username"),
							email = request.POST.get("email"),
							password = make_password(request.POST.get("password"))

				)
			messages.success(request, 'User created successfully.')
			return render(request,'static/signup.html')
	else:
		messages.error(request, 'Password and conform pasword did not match')
		return render(request,'static/signup.html')

def about_journal(request):
	return render(request,'static/about-journal.html')

def about_open(request):
	return render(request,'static/about-open.html')

def about_peer(request):
	return render(request,'static/about-peer.html')

def archive_fulltext(request):
	return render(request,'static/archive-fulltext.html')

def archive(request):
	archive_qs = Archive.objects.all()
	return render(
			request,
			'static/archive.html',
			context={'archive_qs':archive_qs
			}
			)

def article_processing(request):
	return render(request,'static/article-processing.html')

def articles_fulltext(request):
	return render(request,'static/articles-fulltext.html')

def articles(request):
	return render(request,'static/articles.html')

def articlesinpress(request):
	return render(request,'static/articlesinpress.html')

def author_guidelines(request):
	return render(request,'static/author-guidelines.html')	

def benefits(request):
	return render(request,'static/benefits.html')

def collaborations(request):
	return render(request,'static/collaborations.html')

def company_information(request):
	return render(request,'static/company-information.html')

def contact(request):
	return render(request,'static/contact.html')

def current_issue(request):
	current_issues_qs = CurrentIssues.objects.all()
	return render(
			request,
			'static/current-issue.html',
			context={'current_issues_qs':current_issues_qs}
			)

def current_issue_fulltext(request):
	return render(request,'static/current-issuse-fulltext.html')

def ebooks(request):
	return render(request,'static/ebooks.html')

def editor_guidelines(request):
	return render(request,'static/editor-guidelines.html')

def editor_board(request):
	pub_name = request.GET.get("publication_name")
	editors_qs = EditorialBoard.objects.filter(
					publication__publication_name=pub_name)
	return render(
			request,
			'static/editorial-board.html',
			context={"editors_qs":editors_qs}
			)

def faqs(request):
	return render(request,'static/faqs.html')

def indexing(request):
	return render(request,'static/indexing.html')

def membership(request):
	return render(request,'static/membership.html')

def peer_review(request):
	return render(request,'static/peer-review.html')

def publication_ethics(request):
	return render(request,'static/publication-ethics.html')

def publications(request):
	publication_qs = Publication.objects.all()
	# publication_nmaes = {}
	# for single_publication in publication_qs:
	# 	pub_name = single_publication.publication_name

	return render(
		request,
		'static/publications.html',
		context={"publication_qs":publication_qs}
		)

def registration_details(request):
	return render(request,'static/registration-details.html')

def reprints(request):
	return render(request,'static/reprints.html')

def review_guidelines(request):
	return render(request,'static/reviewer-guidelines.html')

def signin(request):
	return render(request,'static/signin.html')

def special_issue(request):
	return render(request,'static/special-issue.html')

def submit_articles(request):
	return render(request,'static/submit-articles.html')

def article_submit(request):
	if request.method == "POST":
		title = request.POST.get("title")
		full_name = request.POST.get("full_name")
		university = request.POST.get("university")
		affilliation =  request.POST.get("affilliation")
		email = request.POST.get("email") 
		phone_no = request.POST.get("phone_no")
		choose_journal = request.POST.get("choose_journal")
		article_type = request.POST.get("article_type")
		article_title = request.POST.get("article_title")
		attachment_article = request.FILES.get("attachment_article")
		if title and full_name and university and email:
			article_qs = Article.objects.create(
						title=title,
						full_name=full_name,
						university=university,
						affilliation=affilliation,
						email=email,
						phone_no=phone_no,
						choose_journal=choose_journal,
						article_type=article_type,
						article_title=article_title,
						attachment_article=attachment_article
						)
			messages.success(request, 'Article Posted successfully.')
			return render(request,'static/submit-articles.html')
		else:
			messages.success(request, 'Please fill all details')
			return render(request,'static/submit-articles.html')

def contact_submit(request):
	if request.method == "POST":
		name = request.POST.get("name")
		email =request.POST.get("email")
		phone_no =request.POST.get("phone_no")
		message =request.POST.get("message")

		contact_us_qs = ContactUs.objects.create(
						name=name,
						email=email,
						phone_no=phone_no,
						message=message
						)

		messages.success(request, 'Thanks for Contacting us.')
		return render(request,'static/contact.html')