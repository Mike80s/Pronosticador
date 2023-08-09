from django.shortcuts import render
from tiendaonline.gestionpedidos.forms import MyForm

def my_view(request):
    form = MyForm()
    return render(request, 'my_template.html', {'form': form})
