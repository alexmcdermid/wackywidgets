from django.shortcuts import render
from .forms import WidgetForm

def index(request):
    widgetForm = WidgetForm()
    return render(request, 'index.html',{'widgetForm':widgetForm})