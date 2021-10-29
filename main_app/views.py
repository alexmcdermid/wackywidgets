from django.shortcuts import render
from .models import Widget
from .forms import WidgetForm

def index(request):
    widgetForm = WidgetForm()
    widgets = Widget.objects.all()
    return render(request, 'index.html',{'widgetForm':widgetForm,'widgets':widgets})