from django.contrib import admin

from .models import Query, Evidence, Gene, Reviewer

admin.site.register(Query)
admin.site.register(Evidence)
admin.site.register(Gene)
admin.site.register(Reviewer)
