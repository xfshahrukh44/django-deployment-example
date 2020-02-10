from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic, Webpage, AccessRecord, User

# Create your views here.
def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpages_list}
    context = {'insert_me': 'hello from views.py 24:8'}
    return render(request, 'first_app/index.html', context = date_dict)

def users(request):
    users_list = User.objects.order_by('first_name')
    user_dict = {'users': users_list}
    return render(request, 'first_app/users.html', context = user_dict)
