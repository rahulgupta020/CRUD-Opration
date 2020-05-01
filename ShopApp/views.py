from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Productdb
from .forms import ProductForm

def create(request):
    if request.method=='POST':
        form=ProductForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/list')
            except:
                pass
    else:
        form=ProductForm()
    return render(request, 'create.html', {'form':form})

def list(request):
    products=Productdb.objects.all()
    return render(request, 'list.html', {'products':products})

def edit(request, id):
    product=Productdb.objects.get(id=id)
    return render(request, 'edit.html', {'product':product})

def update(request, id):
    product=Productdb.objects.get(id=id)
    form=ProductForm(request.POST, instance=product)
    if form.is_valid():
        form.save()
        return redirect("/list")
    return render(request, 'edit.html', {'product':product})

def delete(request, id):
    product=Productdb.objects.get(id=id)
    if request.method == 'POST': 
        product.delete() 
        return redirect("/list")
    return render(request, 'delete1.html', {'object':product})


def delete1(request):
    return render(request, 'delete1.html')
                                         
