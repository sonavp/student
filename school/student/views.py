from django.shortcuts import render,redirect
from django.views.generic import View
from student.forms import Studentform,Courseform
from student.models import student,course
# Create your views here.


class studentview(View):
    def get(self,request,*args,**kwargs):
        form=Studentform()
        return render(request,"student.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=Studentform(request.POST)
        if form.is_valid():
            form.save()
        return render(request,"student.html",{"form":form})
    
class courseview(View):
    def get(self,request,*args,**kwargs):
        form=Courseform()
        return render(request,"course.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=Courseform(request.POST)
        if form.is_valid():
            form.save()
        return render(request,"course.html",{"form":form})
        
class studentlistview(View):
    def get(self,request,*args,**kwargs):
        data=student.objects.all()
        return render(request,"studentlist.html",{"data":data})

class courselistview(View):
    def get(self,request,*args,**kwargs):
        data=course.objects.all()
        return render(request,"courselist.html",{"data":data})
    
class studentupdateview(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        data=student.objects.get(id=id)
        form=Studentform(instance=data)
        return render(request,"studentupdate.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        data=student.objects.get(id=id)
        form=Studentform(request.POST,instance=data)
        if form.is_valid():
            form.save()
            print("yess")
        return redirect("slist")
    
class studentdeleteview(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        student.objects.get(id=id).delete()
        return redirect("slist")
    
class courseupdateview(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        data=course.objects.get(id=id)
        form=Courseform(instance=data)
        return render(request,"courseupdate.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        data=course.objects.get(id=id)
        form=Courseform(request.POST,instance=data)
        if form.is_valid():
            form.save()
            print("yess")
        return redirect("clist")
    
class coursedeleteview(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        course.objects.get(id=id).delete()
        return redirect("clist")