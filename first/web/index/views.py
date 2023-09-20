from re import S, search
import string
from this import s
from tokenize import Name
from unicodedata import name
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm #註冊表單
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.http import HttpResponse
from django.template import context
from django.views.generic import TemplateView, ListView
from .models import classform, classform2
from django.db.models import Q
from django.contrib.auth import get_user_model
from django.db.models import Sum



#註冊
def sign_up(request):
    
    form = UserCreationForm()

    if request.method =="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form': form
    }
    return render(request, 'register.html', context)
 
#確認有無使用者
def index(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('Home')
        else:
            messages.info(request,"帳號或密碼錯誤")

        context={}
        return render(request,'index.html',context)
    return render(request,'index.html')

#首頁
def home(request):
    return render(request, 'home.html') 


#篩選任一星期空堂
def sr(request):
    a=["第一堂","第二堂","第三堂","第四堂","第五堂","第六堂","第七堂","第八堂"]
    b=[]
    data=[]
    if request.method=='GET':
        
        search=request.GET.get('semester')
        search1=request.GET.get('week')
        #1-1
        if search=='110-1'and search1=='mon':  
            for i in range(0,len(a)):
              
                b.append(classform.objects.filter(Q(Mon__contains=a[i])))
                data.append(classform.objects.filter(Q(Mon__contains=a[i])).count())

            context={'data':b[0],'datas':data[0],'data2':b[1],'datas2':data[1],'data3':b[2],'datas3':data[2],'data4':b[3],'datas4':data[3],'data5':b[4],'datas5':data[4],'data6':b[5],'datas6':data[5],'data7':b[6],'datas7':data[6],'data8':b[7],'datas8':data[7]}
               
            return render(request,'home.html',context)
        #1-2        
        elif search=='110-1'and search1=='tue':
               for i in range(0,len(a)):
               
                 b.append(classform.objects.filter(Q(Tue__contains=a[i])))
                 data.append(classform.objects.filter(Q(Tue__contains=a[i])).count())

               context={'data':b[0],'datas':data[0],'data2':b[1],'datas2':data[1],'data3':b[2],'datas3':data[2],'data4':b[3],'datas4':data[3],'data5':b[4],'datas5':data[4],'data6':b[5],'datas6':data[5],'data7':b[6],'datas7':data[6],'data8':b[7],'datas8':data[7]}
               
               return render(request,'home.html',context)
        #1-3       
        elif search=='110-1'and search1=='wed':
               for i in range(0,len(a)):
               
                 b.append(classform.objects.filter(Q(Wed__contains=a[i])))
                 data.append(classform.objects.filter(Q(Wed__contains=a[i])).count())

               context={'data':b[0],'datas':data[0],'data2':b[1],'datas2':data[1],'data3':b[2],'datas3':data[2],'data4':b[3],'datas4':data[3],'data5':b[4],'datas5':data[4],'data6':b[5],'datas6':data[5],'data7':b[6],'datas7':data[6],'data8':b[7],'datas8':data[7]}
               
               return render(request,'home.html',context)
        #1-4 
        elif search=='110-1'and search1=='thu':
               for i in range(0,len(a)):
               
                 b.append(classform.objects.filter(Q(Thu__contains=a[i])))
                 data.append(classform.objects.filter(Q(Thu__contains=a[i])).count())

               context={'data':b[0],'datas':data[0],'data2':b[1],'datas2':data[1],'data3':b[2],'datas3':data[2],'data4':b[3],'datas4':data[3],'data5':b[4],'datas5':data[4],'data6':b[5],'datas6':data[5],'data7':b[6],'datas7':data[6],'data8':b[7],'datas8':data[7]}
               
               return render(request,'home.html',context)
        #1-5
        elif search=='110-1'and search1=='fri':
               for i in range(0,len(a)):
               
                 b.append(classform.objects.filter(Q(Fri__contains=a[i])))
                 data.append(classform.objects.filter(Q(Fri__contains=a[i])).count())

               context={'data':b[0],'datas':data[0],'data2':b[1],'datas2':data[1],'data3':b[2],'datas3':data[2],'data4':b[3],'datas4':data[3],'data5':b[4],'datas5':data[4],'data6':b[5],'datas6':data[5],'data7':b[6],'datas7':data[6],'data8':b[7],'datas8':data[7]}
               
               return render(request,'home.html',context)
        #2-1
        elif search=='110-2'and search1=='mon':
               for i in range(0,len(a)):
               
                 b.append(classform2.objects.filter(Q(Mon__contains=a[i])))
                 data.append(classform2.objects.filter(Q(Mon__contains=a[i])).count())

               context={'data':b[0],'datas':data[0],'data2':b[1],'datas2':data[1],'data3':b[2],'datas3':data[2],'data4':b[3],'datas4':data[3],'data5':b[4],'datas5':data[4],'data6':b[5],'datas6':data[5],'data7':b[6],'datas7':data[6],'data8':b[7],'datas8':data[7]}
               
               return render(request,'home.html',context)
        #2-2
        elif search=='110-2'and search1=='tue':
               for i in range(0,len(a)):
               
                 b.append(classform2.objects.filter(Q(Tue__contains=a[i])))
                 data.append(classform2.objects.filter(Q(Tue__contains=a[i])).count())

               context={'data':b[0],'datas':data[0],'data2':b[1],'datas2':data[1],'data3':b[2],'datas3':data[2],'data4':b[3],'datas4':data[3],'data5':b[4],'datas5':data[4],'data6':b[5],'datas6':data[5],'data7':b[6],'datas7':data[6],'data8':b[7],'datas8':data[7]}
               
               return render(request,'home.html',context)
        #2-3      
        elif search=='110-2'and search1=='wed':
               for i in range(0,len(a)):
               
                 b.append(classform2.objects.filter(Q(Wed__contains=a[i])))
                 data.append(classform2.objects.filter(Q(Wed__contains=a[i])).count())

               context={'data':b[0],'datas':data[0],'data2':b[1],'datas2':data[1],'data3':b[2],'datas3':data[2],'data4':b[3],'datas4':data[3],'data5':b[4],'datas5':data[4],'data6':b[5],'datas6':data[5],'data7':b[6],'datas7':data[6],'data8':b[7],'datas8':data[7]}
               
               return render(request,'home.html',context)
        #2-4 
        elif search=='110-2'and search1=='thu':
               for i in range(0,len(a)):
               
                 b.append(classform2.objects.filter(Q(Thu__contains=a[i])))
                 data.append(classform2.objects.filter(Q(Thu__contains=a[i])).count())

               context={'data':b[0],'datas':data[0],'data2':b[1],'datas2':data[1],'data3':b[2],'datas3':data[2],'data4':b[3],'datas4':data[3],'data5':b[4],'datas5':data[4],'data6':b[5],'datas6':data[5],'data7':b[6],'datas7':data[6],'data8':b[7],'datas8':data[7]}
               
               return render(request,'home.html',context)
        #2-5
        elif search=='110-2'and search1=='fri':

               for i in range(0,len(a)):
               
                 b.append(classform.objects.filter(Q(Fri__contains=a[i])))
                 data.append(classform.objects.filter(Q(Fri__contains=a[i])).count())

               context={'data':b[0],'datas':data[0],'data2':b[1],'datas2':data[1],'data3':b[2],'datas3':data[2],'data4':b[3],'datas4':data[3],'data5':b[4],'datas5':data[4],'data6':b[5],'datas6':data[5],'data7':b[6],'datas7':data[6],'data8':b[7],'datas8':data[7]}
               
               return render(request,'home.html',context)
        
        else:
            context={}
            return render(request,'home.html',context)
    else:
            context={}
            return render(request,'home.html',context)
 
        
#字串加總
def add(a):
    s=""
    for i in range(a):
        s+=i
    return s

#登出
def log_out(request):
    if request.method == "POST":
      logout(request)
      index(request)
    else:
        return render(request,'logout.html')
    
    return render(request,'logout.html')

#所有
def all(request):
    if request.method=='GET':
           search=request.GET.get('semester')
           a=["第一堂","第二堂","第三堂","第四堂","第五堂","第六堂","第七堂","第八堂"]
           mon=[]
           tue=[]
           wed=[]
           thu=[]
           fri=[]
           if search=='110-1':
            
            count=classform.objects.all().count()
           
            for i in range(len(a)):
               mon.append(classform.objects.filter(Q(Mon__contains=a[i])).count())
               tue.append(classform.objects.filter(Q(Tue__contains=a[i])).count())
               wed.append(classform.objects.filter(Q(Wed__contains=a[i])).count())
               thu.append(classform.objects.filter(Q(Thu__contains=a[i])).count())
               fri.append(classform.objects.filter(Q(Fri__contains=a[i])).count())
            context={'count':count,'mon':mon,'tue':tue,'wed':wed,'thu':thu,'fri':fri}
            return render(request,'all.html',context) 
           elif search=='110-2':
             count=classform2.objects.all().count()
             for i in range(len(a)):
               mon.append(classform2.objects.filter(Q(Mon__contains=a[i])).count())
               tue.append(classform2.objects.filter(Q(Tue__contains=a[i])).count())
               wed.append(classform2.objects.filter(Q(Wed__contains=a[i])).count())
               thu.append(classform2.objects.filter(Q(Thu__contains=a[i])).count())
               fri.append(classform2.objects.filter(Q(Fri__contains=a[i])).count())
             context={'count':count,'mon':mon,'tue':tue,'wed':wed,'thu':thu,'fri':fri}
             return render(request,'all.html',context) 
           else:
             context={}
             return render(request,'all.html',context) 
#介紹                
def intro(request):
    return render(request,'intro.html')

    