from django.shortcuts import render

def show_main(request):
    context = {
        'name' : 'gigi vibranium',
        'price': '2.000.000.000.000.00',
        'description': 'barang ini berguna untuk keseharian,mampu membantu nengunyah apapun',
        'stock' : '30',
    }

    return render(request, "main.html", context)
