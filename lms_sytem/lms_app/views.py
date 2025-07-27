from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

# Create your views here.


def home(request):
    return render(request, 'home.html',{'current_tab': 'home'})

def readers_tab(request):
    if request.method == "POST":
        if request.method == "POST":
            data = request.POST['querry']
            readers = Reader.objects.raw("select * from lms_app_Reader where reader_name like '%" + data + "%'")
            return render(request, 'readers.html', {'current_tab':'readers', 'readers': readers})
        else:
            messages.success(request, "couldn't find that reader !")
            return redirect('readers')
    else:
        readers = Reader.objects.all()
        return render(request, 'readers.html', {'current_tab':'readers', 'readers': readers})



def save(request):
    student_name = request.POST['student_name']
    return render(request, 'welcome.html',{'student_name':student_name})

def bag(request):
    return render(request, 'bag.html',{'current_tab': 'bag'})

def returns(request):
    return render(request, 'returns.html',{'current_tab': 'returns'})

def books(request):
    return render(request, 'books.html',{'current_tab': 'books'})

def save_reader(request):
    if request.method == 'POST':
        reader = Reader(refrence_id = request.POST['reader_ref_id'],
                     reader_name = request.POST['reader_name'],
                     reader_contact = request.POST['reader_contact'],
                     reader_address = request.POST['address'],
                     is_active = True
                     )
        reader.save()
        messages.success(request, 'New reader saved successfully')
    return redirect('readers')



