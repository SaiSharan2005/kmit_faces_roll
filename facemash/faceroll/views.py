from django.shortcuts import render
from django.http import HttpResponse
from .forms import SearchForm

# Create your views here.

def home(request):
    if request.method =="POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['roll_no'].upper()
            img_url = f"http://teleuniv.in/sanjaya/student-images/{query}.jpg"
            form= SearchForm()

            return render(request, 'home.html',{"img_url":img_url,"query":query,"bool":True,'form':form})
    else:
        form= SearchForm()
        return render(request,'home.html',{'form':form})


    # return render(request,"home.html")
