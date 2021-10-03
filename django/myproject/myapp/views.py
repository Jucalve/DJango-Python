from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    #return HttpResponse('<h1>Hey, Welcome</h1>') #Here is the page from urls in myapp
                                                 #And I can have n number of function in n number of urls
                                                 #Opening the html file in templates folder
                                                 #It's really easy to send variables here xd
    context = {                                  #diccionaries rules!
        'name': 'Lala',
        'age': 24,
        'comment': 'Biutifull princess baby',
    }
    return render(request, 'index.html', context)
    
def something(request):
    aux = request.POST['text']
    context = {
        'words' : aux,
        'num_words' : len(aux.split()),
    }
    return render(request, 'something.html', context)