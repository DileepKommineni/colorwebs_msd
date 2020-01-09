"""colorwebs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from colorapp import views
from colorwebs import settings

urlpatterns = [
    path('admin/', admin.site.urls),

    #Sign up page
 	path('signup/', views.signup_user, name="signup-user"),
 	# Signup submit
 	path('signup/submit/', views.signup_submit, name="signup-submit"),

    path('home',views.home,name="home"),
    path('about_journal',views.about_journal,name="about_journal"),

    path('about_open',views.about_open,name="about_open"),
    path('about_peer',views.about_peer,name="about_peer"),
    path('archive_fulltext',views.archive_fulltext,name="archive_fulltext"),
    path('archive',views.archive,name="archive"),
    path('article_processing',views.article_processing,name="article_processing"),
    path('articles_fulltext',views.articles_fulltext,name="articles_fulltext"),
    path('articles',views.articles,name="articles"),
    path('articlesinpress',views.articlesinpress,name="articlesinpress"),
    path('author_guidelines',views.author_guidelines,name="author_guidelines"),
    path('benefits',views.benefits,name="benefits"),
    path('collaborations',views.collaborations,name="collaborations"),
    path('company_information',views.company_information,name="company_information"),
    path('contact',views.contact,name="contact"),
    path('current_issue',views.current_issue,name="current_issue"),
    path('current_issue_fulltext',views.current_issue_fulltext,name="current_issue_fulltext"),
    path('ebooks',views.ebooks,name="ebooks"),
    path('editor_guidelines',views.editor_guidelines,name="editor_guidelines"),
    path('editor_board',views.editor_board,name="editor_board"),
    path('faqs',views.faqs,name="faqs"),
    path('indexing',views.indexing,name="indexing"),
    path('membership',views.membership,name="membership"),
    path('peer_review',views.peer_review,name="peer_review"),
    path('publication_ethics',views.publication_ethics,name="publication_ethics"),
    path('publications',views.publications,name="publications"),
    path('registration_details',views.registration_details,name="registration_details"),
    path('reprints',views.reprints,name="reprints"),
    path('reviewer_guidelines',views.review_guidelines,name="review_guidelines"),
    path('signin',views.signin,name="signin"),
    path('special_issue',views.special_issue,name="special_issue"),
    path('submit_articles',views.submit_articles,name="submit_articles"),

    path('contact_submit',views.contact_submit,name="contact_submit"),
    path('article_submit',views.article_submit,name="article_submit"),

] + static(settings.STATIC_URL,  document_root=settings.STATIC_ROOT)