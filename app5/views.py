from django.shortcuts import render,get_object_or_404
from django.http import JsonResponse
from .models import Bozorlar,OnlineDokonlar


# Create your views here.
def all(request):
    all = OnlineDokonlar.objects.all()
    result = []
    for i in all:
        result.append({
            'name':i.name,
            'who_created':i.who_created,
            'when_created':i.when_created
        })
    return JsonResponse(result,safe =False)

def detail(request,detail_id):
    each = Bozorlar.objects.get(id=detail_id)
    each = get_object_or_404(Bozorlar,id=detail_id)
    info = f'bozor nomi:{Bozorlar.name}, {Bozorlar.build_in} da qurilgan'
    return JsonResponse(info)
