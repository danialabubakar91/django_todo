from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def signupuser(request):
    if request.method == 'GET':
        return render(request, 'todo/signupuser.html', {'form':UserCreationForm()})