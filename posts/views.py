
# Django
from django.shortcuts import render
from django.http import HttpResponse

#Utilities
from datetime import datetime

posts =[

    {
        'name': 'Mont Blank',
        'user': 'Ninaia',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/id/1000/200/300',
    },

    {
        'name': 'Some Other',
        'user': 'Denden',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/id/1015/200/300',
    },

    {
        'name': 'Other More',
        'user': 'Ninaia',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/id/1019/200/300',
    }


]



def list_post(request):
    content = []
    for post in posts:
        content.append("""
        <p><strong>{name}</strong></p>
        <p><small>{user} - <i>{timestamp}</i></small></p>
        <figure><img src="{picture}"/></figure>
        """.format(**post))
    return HttpResponse('<br>'.join(content))