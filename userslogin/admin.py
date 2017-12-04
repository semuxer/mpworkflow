from django.contrib import admin
from .models import Department, User, NewsPaper, Paper, Acces
# Register your models here.

admin.site.register(Department)
admin.site.register(User)
admin.site.register(NewsPaper)
admin.site.register(Acces)
admin.site.register(Paper)