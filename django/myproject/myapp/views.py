from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature

# Create your views here.
def index(request):
    #return HttpResponse('<h1>Hey, Welcome</h1>') #Here is the page from urls in myapp
                                                 #And I can have n number of function in n number of urls
                                                 #Opening the html file in templates folder
                                                 #It's really easy to send variables here xd
    #context = {                                  #diccionaries rules!
    #    'name': 'Lala',
    #    'age': 24,
    #    'comment': 'Biutifull princess baby',
    #}
    feature1 = Feature()
    feature1.id=0
    feature1.name='Lala Andrea'
    feature1.details='Preciosa Princesa Bebe'

    feature2 = Feature()
    feature2.id=1
    feature2.name='python'
    feature2.details='Keep coding to keep learning'

    feature3 = Feature()
    feature3.id=2
    feature3.name='React'
    feature3.details='Watch OSRH videos'

    feature4 = Feature()
    feature4.id=3
    feature4.name='Dont Starve'
    feature4.details='Study'

    features = [feature1, feature2, feature3, feature4]
    return render(request, 'index.html', {'features': features})
    
def something(request):
    aux = request.POST['text']
    context = {
        'words' : aux,
        'num_words' : len(aux.split()),
    }
    return render(request, 'something.html', context)