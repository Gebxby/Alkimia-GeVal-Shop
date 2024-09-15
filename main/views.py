from django.shortcuts import render,redirect   # Tambahkan import redirect di baris ini
from main.forms import MenutokoForm
from main.models import Menutoko
from django.http import HttpResponse
from django.core import serializers

def show_main(request):
    menu_entries = Menutoko.objects.all()

    context = {
        'name' : 'gigi vibranium',
        'price': '2.000.000.000.000.00',
        'description': 'barang ini berguna untuk keseharian,mampu membantu nengunyah apapun',
        'stock' : '30',
        'menu_entries' : menu_entries

    }

    return render(request, "main.html", context)
def create_menu(request):
    form = MenutokoForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create.html", context)

def show_xml(request):
    data = Menutoko.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
def show_json(request):
    data = Menutoko.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
def show_xml_by_id(request, id):
    data = Menutoko.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
def show_json_by_id(request, id):
    data = Menutoko.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
