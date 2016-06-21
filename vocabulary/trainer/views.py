from django.db.backends.dummy.base import IntegrityError
from django.http.response import HttpResponse
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect
import pdb;

# Create your views here.
from django.template import loader, RequestContext
from django.views.decorators.csrf import ensure_csrf_cookie

from forms import UserCreateForm, LoginForm, UploadFileForm
from trainer.models import Word, Language


def index(request):
    context = RequestContext(request)
    return HttpResponse(render(request, 'trainer/index.html', context))

def register_user(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user = form.save()
            return HttpResponse("yeah!")

    else:
        form = UserCreateForm()

    return render(request, 'trainer/register.html', {'form':form})


def login_user(request):
    #pdb.set_trace()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            print "Success!"
            login(request,user)
        context = RequestContext(request)
        return HttpResponse(render(request, 'trainer/index.html', context))

    else:
        form = LoginForm()
        return render(request, 'trainer/login.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('index')


def populate_words(request):
    if request.method == 'POST':
        language = Language.objects.get(name=request.POST['language'])
        file = request.FILES['file']
        words = []
        for line in file:
            if line == "\n" or line == " \n":
                continue
            word = Word(word=line, language=language)
            words.append(word.word)
            try:
                word.save()
            except:
                IntegrityError()


        context = {"words": words}
        return render(request, 'trainer/upload_success.html', context)


    else:
        form = UploadFileForm()
        return render(request, 'trainer/populate.html', {'form': form})


    return render(request, 'trainer/populate.html')

def upload_success():
    print "Success!"