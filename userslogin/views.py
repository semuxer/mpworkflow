from django.shortcuts import render
from .models import Department, User, NewsPaper, Paper, Acces

# Create your views here.
def np_list(request):
    newspapers = NewsPaper.objects.all().order_by('createdatetime')
    return render(request, 'np_list.html', {'newspapers':newspapers})