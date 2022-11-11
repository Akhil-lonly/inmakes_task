from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView, DeleteView

from .forms import update_task
from . models import task
from django.views.generic.list import ListView
# Create your views here.
class tasklist_view(ListView):
    model = task
    template_name = 'index.html'
    context_object_name = 'task1'

class taskdetail(DetailView):
    model = task
    template_name = 'detail.html'
    context_object_name = 'task1'

class taskupdate(UpdateView):
    model = task
    template_name = 'update.html'
    context_object_name = 'task1'
    fields = ('name','priority','date')
    def get_success_url(self):
        return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})


class taskdelete(DeleteView):
    model = task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvhome')

def index(request):
    task1=task.objects.all()

    if request.method=='POST':
        name=request.POST.get('name','')
        priority=request.POST.get('priority','')
        date=request.POST.get('date','')
        task2=task(name=name,priority=priority,date=date)
        task2.save()

    return render(request,'index.html',{'task1':task1})

def delete(request,id):
    task1=task.objects.get(id=id)
    if request.method=='POST':
        task1.delete()
        return redirect('/')

    return render(request,'delete.html')


def update(request,id):
    task1=task.objects.get(id=id)
    newtask=update_task(request.POST or None,instance=task1)
    if newtask.is_valid():
       newtask.save()
       return redirect('/')
    return render(request,'edit.html',{'task1':task1,'newtask':newtask})
