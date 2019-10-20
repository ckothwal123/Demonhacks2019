from django.contrib import admin
from .models import Source, Dest, Resources, Result

admin.site.register(Source)
admin.site.register(Dest)
admin.site.register(Resources)
admin.site.register(Result)