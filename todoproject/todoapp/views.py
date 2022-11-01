from django.shortcuts import render, redirect
from .models import Task
from .forms import todoform
# Create your views here.
def home(request):
    t1 = Task.objects.all()
    if request.method=='POST':
        name = request.POST.get('task','')
        p = request.POST.get('priority','')
        d=request.POST.get('date','')
        t = Task(name=name,priority=p,date=d)
        t.save()
    return render(request,"home.html",{'task':t1})

def delete(request, taskid):
    b=Task.objects.get(id=taskid)
    if request.method=='POST':
        b.delete()
        return redirect('/')
    return render(request,"delete.html")
def update(request,taskid):
    b = Task.objects.get(id=taskid)
    f=todoform(request.POST or None,instance=b)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request, "Update.html",{'key1':f,'t_id':b})
def detail(request):
    return render(request,"detail.html",)