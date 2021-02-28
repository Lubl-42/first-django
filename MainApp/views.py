from django.shortcuts import render, HttpResponse

items = [
   {"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
   {"id": 2, "name": "Куртка кожаная" ,"quantity":2},
   {"id": 3, "name": "Coca-cola 1 литр" ,"quantity":12},
   {"id": 4, "name": "Картофель фри" ,"quantity":0},
   {"id": 5, "name": "Кепка" ,"quantity":124},
]

from MainApp.models import Item

user = {'name':'Ivan','sec_name':'Petrovich','surname':'Ivanov'}

# Create your views here.
def main(request):
    return render(request,'index.html')




def show_item (request,id):
    try:
        current_item= Item.object.get(id=id)
    except ObjectDoesNotExist:
        raise Http404
    context={"item":current_item}
    return render(request, 'test.html', context)


def items_list (request):
    context={'items': Item.objects.all()}
    return render(request,'items.html',context)