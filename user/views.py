from django.shortcuts import render, HttpResponseRedirect
from .forms import UserForm
from .models import UserModel

# Create your views here.
def index(request):
    if(request.method == 'POST'):
        form = UserForm(request.POST)
        if(form.is_valid()):
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            age = form.cleaned_data['age']
            reg = UserModel(name=name, email=email, age=age)
            reg.save()
            form = UserForm()
    else:
        form = UserForm()
        
    data = UserModel.objects.all()
    display_data = {
        'form': form,
        'data': data
    }
    return render(request, 'user/index.html', display_data)

def delete(request, id):
    pi = UserModel.objects.get(pk=id)
    pi.delete()
    return HttpResponseRedirect('/')

def edit(request, id):
    pi = UserModel.objects.get(pk=id)
    if(request.method == 'POST'):
        form = UserForm(request.POST, instance=pi)
        if(form.is_valid()):
            form.save()
        return HttpResponseRedirect('/')
    else:
        form = UserForm(instance=pi)
        return render(request, 'user/edituser.html', {'form':form})