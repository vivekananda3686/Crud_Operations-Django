from django.shortcuts import render,redirect
from Crud_App.models import Student

# Create your views here.
def homepage(request):
    t=Student.objects.all()
    if request.method=="POST":
        a=request.POST['rn']
        b=request.POST['sn']
        c=request.POST['em']
        d=request.POST['yr']
        e=request.POST['br']
        w=Student.objects.create(roll=a,sname=b,email=c,year=d,branch=e)
        return redirect('/')
    return render(request,'static/homepage.html',{'v':t})

def deldata(request,a):
    x=Student.objects.get(id=a)
    if request.method=="POST":
        x.delete()
        return redirect('/')
    return render(request,'static/delete.html',{'c':x})

def update(request,b):
    z=Student.objects.get(id=b)
    if request.method=="POST":
        z.sname=request.POST['s']
        z.email=request.POST['e']
        z.year=request.POST['y']
        z.branch=request.POST['b']
        z.save()
        return redirect('/')
    return render(request,'static/update.html',{'d':z})