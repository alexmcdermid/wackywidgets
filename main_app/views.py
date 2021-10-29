from django.shortcuts import redirect, render
from .models import Widget
from .forms import WidgetForm

def index(request):
    widgetForm = WidgetForm()
    widgets = Widget.objects.all()
    count = 0
    for widget in widgets:
        count+=widget.quantity
    return render(request, 'index.html',{'widgetForm':widgetForm,'widgets':widgets,'count':count})

def handleForm(request):
    form = WidgetForm(request.POST)
    if form.is_valid():
        newWidget = form.save()
        newWidget.save()
    return redirect('index')

def delete(request, widget_id):
    Widget.objects.filter(id=widget_id).delete()
    return redirect('index')
