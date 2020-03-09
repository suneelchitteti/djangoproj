from django.shortcuts import render
from django.http import HttpResponse
from .models import registration
from .forms import registrationform
from .forms import Loginform
def home(request):
    return render(request,'home.html')
def reg(request):
    if request.method=='POST':
        form=registrationform(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponse('registration sucessfully competed')
        else:
            print(form.errors)
            return HttpResponse("registration not completed")
    else:
        form=registrationform()
        return render(request,'reg.html',{'form':form})
def login(request):
    if request.method=='POST':
        myloginform=Loginform(request.POST)
        if myloginform.is_valid():
            un=myloginform.cleaned_data['user']
            pw=myloginform.cleaned_data['Pwd']
            dbuser=registration.objects.filter(user=un,Pwd=pw)
            if not dbuser:
                return HttpResponse('login faild')
            else:
                return HttpResponse('login sucess')
    else:
        form=Loginform()
        return HttpResponse(request, 'login.html',{'form':form})