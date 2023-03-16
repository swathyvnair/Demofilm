from django.http import HttpResponse
from django.shortcuts import render, redirect
from.models import Film
from.forms import Filmform
# Create your views here.
def index(request):
    film=Film.objects.all()
    context={
        'film_list':film
    }
    return render(request,'index.html',context)
def detail(request,film_id):
    film=Film.objects.get(id=film_id)
    return render(request,"detail.html",{'film':film})

def add_film(request):
    if request.method=="POST":
        name=request.POST.get('name',)
        desc = request.POST.get('desc', )
        year = request.POST.get('year', )
        img = request.FILES['img']
        film=Film(name=name,desc=desc,year=year,img=img)
        film.save()
    return render(request,'add.html')

def update(request,id):
    film=Film.objects.get(id=id)
    form=Filmform(request.POST or None, request.FILES,instance=film)
    if form.is_valid():
        form.save()
        return   redirect('/')
    return render(request,'edit.html',{'form':form,'film':film})

def delete(request,id):
    if request.method=='POST':
        film=Film.objects.get(id=id)
        movie.delete()
        return  redirect('/')
    return render(request,'delete.html')
