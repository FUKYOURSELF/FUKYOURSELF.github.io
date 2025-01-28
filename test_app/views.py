from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
from django.http import HttpResponse

def function_view_test(request):
    return HttpResponse('<h1>Hello World! Function-based View Test</h1>')

class ClassViewTest(TemplateView):
    template_name= 'test.html'
    
def book_query(request):
    book_id=request.GET.get('id')
    book_name=request.GET.get('name')
    return HttpResponse(f'你查找的书是{book_id}号书,名称为《{book_name}》')

def book_query1(request,book_id):
    return HttpResponse(f'你查找的书是{book_id}号书')

