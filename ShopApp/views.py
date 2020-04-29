from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Productdb
from .forms import ProductForm

def index(request):
    if request.method=='POST':
        form=ProductForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form=ProductForm()
    return render(request, 'index.html', {'form':form})

def show(request):
    products=Productdb.objects.all()
    return render(request, 'show.html', {'products':products})

def edit(request, id):
    product=Productdb.objects.get(id=id)
    return render(request, 'edit.html', {'product':product})

def update(request, id):
    product=Productdb.objects.get(id=id)
    form=ProductForm(request.POST, instance=product)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, 'edit.html', {'product':product})

def delete(request, id):
    product=Productdb.objects.get(id=id)
    product.delete()
    return redirect("/show")

def delete1(request):
    return render(request, 'delete1.html')
                                         
