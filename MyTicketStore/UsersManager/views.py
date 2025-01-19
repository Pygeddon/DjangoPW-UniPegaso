from django.shortcuts import render
from django.views.generic.base import TemplateView

from .forms import UserRegisterForm, UserResetPasswordForm
# Create your views here.

def register_new_user(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            print('User created')
    else:
        form = UserRegisterForm()
    
    context = {'form': form}

    return render(request, 'registration/register_new_user.html',context)