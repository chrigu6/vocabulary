from django.http.response import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render

# Create your views here.
from django.template import loader
from forms import UserCreateForm


def index(request):
    template = loader.get_template('trainer/index.html')
    return HttpResponse(template.render(request))

def register_user(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user = form.save()
            return HttpResponse("yeah!")

    else:
        form = UserCreateForm()

    return render(request, 'trainer/register.html', {'form':form})
