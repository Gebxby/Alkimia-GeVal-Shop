from django.shortcuts import render, redirect, reverse  # Tambahkan import redirect di baris ini
from main.forms import MenutokoForm
from main.models import Menutoko
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags

@login_required(login_url='/login')
def show_main(request):
    

 

    context = {
        'name' : 'gigi vibranium',
        'price': '2.000.000.000.000.00',
        'description': 'barang ini berguna untuk keseharian,mampu membantu nengunyah apapun',
        'stock' : '30',
        'last_login': request.COOKIES['last_login'],
        
    }

    return render(request, "main.html", context)
def create_menu(request):
    form = MenutokoForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        menu = form.save(commit=False)
        menu.user = request.user
        menu.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create.html", context)


def show_xml(request):
    data = Menutoko.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
def show_json(request):
    data = Menutoko.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
def show_xml_by_id(request, id):
    data = Menutoko.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
def show_json_by_id(request, id):
    data = Menutoko.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)


def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response

    else:
        form = AuthenticationForm(request)
    context = {'form': form}
    return render(request, 'login.html', context)   

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
    

def edit_menu(request, id):
    # Get mood entry berdasarkan id
    menu = Menutoko.objects.get(pk = id)

    # Set mood entry sebagai instance dari form
    form = MenutokoForm(request.POST or None, instance=menu)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_menu.html", context)

def delete_menu(request, id):
    # Get mood berdasarkan id
    menu = Menutoko.objects.get(pk = id)
    # Hapus menu
    menu.delete()
    # Kembali ke halaman awal
    return HttpResponseRedirect(reverse('main:show_main'))

@csrf_exempt
@require_POST
def add_menu_by_ajax(request):
    name = strip_tags(request.POST.get("name")) # strip HTML tags!
    price = strip_tags(request.POST.get("price"))
    description = strip_tags(request.POST.get("description"))
    user = request.user

    new_menu = Menutoko(
        nane=name,price = price,
        description = description,
        user=user
    )
    new_menu.save()

    return HttpResponse(b"CREATED", status=201)