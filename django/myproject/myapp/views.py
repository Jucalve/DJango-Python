from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
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
    features=Feature.objects.all() #From database (models.py) 
    return render(request, 'index.html', {'features': features})

def register(request):
    if request.method == 'POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2'] #We got the info. to make an user on the db

        if password == password2:
            if User.objects.filter(email=email).exists(): #checks if email is already used
                messages.info(request, 'Email Already Used')
                return redirect('register')
            elif User.objects.filter(username=username).exists(): #chechs if usernale is already used
                messages.info(request, 'Username Already Used')
                return redirect('register')
            else:                           #Creates the user
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Password not the same')
            return redirect('register')

    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credentials invalid')
            return redirect('login')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

#def something(request):
#    aux = request.POST['text']
#    context = {
#        'words' : aux,
#        'num_words' : len(aux.split()),
#    }
#    return render(request, 'something.html', context)