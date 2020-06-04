
# Django

from django.shortcuts import render


#Utilities
from datetime import datetime

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