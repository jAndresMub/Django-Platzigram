
#Django
from django.http import HttpResponse
import json
#Utilities
from datetime import datetime



# esta funcion es invocada desde el path
#para que se ejecute se debe importar de django.http el HttpResponse
def hello_word(request):
    
    #se le asigna a now el formato de string a datetime
    # https://docs.python.org/3/library/datetime.html
    
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    
    return HttpResponse('Hello, the time of the server is {now}'.format(
        now=(now)
    ))

def sort_int(request):
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sorted_ints = sorted(numbers)
    data = {
       'status': 'ok',
       'numbers': sorted_ints,
       'message': 'Integers sorted successfully'
    }
    return HttpResponse(json.dumps(data, indent=4), content_type='application/json')
    
     #import pdb; pdb.set_trace()

def say_hi(request, name, age):
    if age < 12:
        message = 'Hello {}, you are not allowed to be here'.format(name)
    else:
        message = 'Hello {}, welcome to platzigram!!!'.format(name)
    return HttpResponse(message)