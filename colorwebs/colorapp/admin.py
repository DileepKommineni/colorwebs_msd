from django.contrib import admin
from .models import (
						ContactUs,
						Article,
						Publication,
						PublicationImages,
						EditorialBoard,
						CurrentIssues,
						Archive,

						)
# Register your models here.

admin.site.register(ContactUs)
admin.site.register(Article)
admin.site.register(Publication)
admin.site.register(PublicationImages)
admin.site.register(EditorialBoard)
admin.site.register(CurrentIssues)
admin.site.register(Archive)