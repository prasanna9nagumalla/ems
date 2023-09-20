from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Student


# Create your views here.
def idt(request):
	return render(request,'html/index.html')
def dy(request):
	return render(request,'html/sample.html')
def btp(request):
	return render(request,'html/home.html')
def about(request):
	return render(request,'html/about.html')
def contact(request):
	return render(request,'html/contact.html')
def loginofemp(request):
	return render(request,'html/login.html')
def workdo(request):
	return render(request,'html/workdone.html')
def register(request):
	if request.method == "POST":
		r = request.POST['rn']
		n = request.POST['nm']
		e = request.POST['em']
		a = request.POST['ag']
		print(r,n,e,a)
		return render(request,'html/display.html',{'a':r,'b':n,'c':e,'d':a})
	return render(request,'html/register.html')
def index(request):
	w = Student.objects.all()
	if request.method == "POST":
		aa = request.POST['r']
		ab = request.POST['n']
		ac = request.POST['y']
		ad = request.POST['b']
		ae = request.POST['a']
		z = Student(sroll=aa,sname=ab,syear=ac,sbranch=ad,sage=ae)
		z.save()
		return redirect('/')
	return render(request,'html/index.html',{'st':w})
def empupdate(request,w):
	f = Student.objects.get(id=w)
	if request.method == "POST":
		#f.sroll = request.POST['r']
		f.sname = request.POST['n']
		f.syear = request.POST['y']
		f.sbranch = request.POST['b']
		f.sage = request.POST['a']
		f.save()
		return redirect('/')
	return render(request,'html/empupdate.html',{'s':f})
def empdelete(request,y):
	p = Student.objects.get(id=y)
	if request.method == "POST":
	    p.delete()
	    return redirect('/')	
	return render(request,'html/empdelete.html',{'h':p})
def home(request):
   return render(request,'html/home.html')	