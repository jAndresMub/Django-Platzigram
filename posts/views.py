
# Django

from django.shortcuts import render
from django.http import HttpResponse

#Utilities
from datetime import datetime

#Local
from posts.models import User

posts =[

    {
        'name': 'Mont Blank',
        'user': 'Ninaia',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/id/100/200/200',
    },

    {
        'name': 'Some Other',
        'user': 'Denden',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/id/1015/200/200',
    },

    {
        'name': 'Other More',
        'user': 'Ninaia',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/id/1011/200/200',
    }


]



def list_post(request):
    content = []
    return render(request, 'feed.html', {'posts': posts})

def ing_post(request,email,passwoed,first_name,last_name):
    usuer = User.objects.create(
        email=email,
        passwoed= passwoed,
        first_name = first_name,
        last_name = last_name

    )

    return HttpResponse(usuer)

    
def queryuno(request, mailusuario):
    mailusuario = User.objects.filter(email__endswith=mailusuario)
    return HttpResponse(mailusuario)