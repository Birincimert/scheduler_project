from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse("Calendar App Ana Sayfa")  # Ana sayfa için basit bir cevap

def upload_excel(request):
    return HttpResponse("Burada Excel yükleme işlemi gerçekleşecek!")
