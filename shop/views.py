from django.shortcuts import render
from .models import Jewelry

# Create your views here.

def HomePage(request):
	#return HttpResponse('<h1>Champignon</h1>')
	jewelry = Jewelry.objects.all()
	listJewelry = []
	for j in jewelry:
		listJewelry.append(j.id)
		j.jewelry_price = "{:,.2f}".format(j.jewelry_price)
	context = {
		'jewelry' : jewelry,
		'amountJewelry' : len(jewelry),
		'listJewelry' : listJewelry
	}
	return render(request,'shop/home.html',context)

def DetailJewelry(request,id):
	jewelry = Jewelry.objects.get(id=id)
	jewelry.jewelry_price = "{:,.2f}".format(jewelry.jewelry_price)
	context={
		"jewelry":jewelry
	}
	return render(request,'shop/detail.html',context)