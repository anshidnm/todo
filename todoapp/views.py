from django.shortcuts import render,redirect
from . models import task
from . forms import todoform
# Create your views here.
def main(request):
    obj=task.objects.order_by('priority')
    if request.method=="POST":
        name=request.POST.get("name")
        priority=request.POST.get("prio")
        date=request.POST.get("date")
        obj1=task(name=name,priority=priority,date=date)
        obj1.save()
    return render(request,'index.html',{'obj':obj})
def delete(request,delete_id):
    obj1=task.objects.get(id=delete_id)
    obj1.delete()
    return redirect("/")
    obj=task.objects.order_by('priority')
    return render(request,'index.html',{'obj':obj})
def update(request,update_id):
    obj1=task.objects.get(id=update_id)
    form=todoform(request.POST or None,instance=obj1)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'obj1':obj1})
