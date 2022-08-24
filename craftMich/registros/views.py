from lib2to3.pgen2.token import OP
import re
from tracemalloc import get_object_traceback
from django.shortcuts import render
from .models import Artesania, Opinion
from .forms import OpinionForm
from django.shortcuts import get_object_or_404
# Create your views here.
def home(request):
    return render(request,"registros/home.html")

def catalogo(request):
    artesania=Artesania.objects.all()
    return render(request,"registros/catalogo.html",{"artesania":artesania})

def opiniones(request):
    opinion=Opinion.objects.all()
    if request.method == 'POST':
        form=OpinionForm(request.POST)
        if form.is_valid():
            form.save()
            opinion=Opinion.objects.all()
            return render(request,"registros/opiniones.html",{"opinion":opinion})
    form=OpinionForm()
    return render(request,"registros/opiniones.html",{'form':form,'opinion':opinion})

def editar(request,id):
    opinion=get_object_or_404(Opinion, id=id)
    form=OpinionForm(request.POST, instance=opinion)
    if form.is_valid():
        form.save()
        opinion=Opinion.objects.all()
        return render(request,'registros/opiniones.html',{"opinion":opinion})
    return render(request,'registros/editarO.html',{"opinion":opinion})

def eliminar(request, id, confirmacion='registros/eliminarO.html'):
    opinion=get_object_or_404(Opinion, id=id)
    if request.method=='POST':
        opinion.delete()
        opinion=Opinion.objects.all()
        return render(request,'registros/opiniones.html',{"opinion":opinion})
    return render(request,confirmacion,{'object':object})