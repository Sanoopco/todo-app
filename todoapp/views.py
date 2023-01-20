from django.shortcuts import render
from todoapp.models import Tasks
from django.views.generic import TemplateView,CreateView,FormView,ListView,View
from django.contrib.auth.views import PasswordChangeView,LogoutView
from todoapp.forms import RegistrationForm,LoginForm,TaskForm,ChangePassswordForm
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.


class UserView(CreateView):
    model=User
    form_class=RegistrationForm
    template_name='registration.html'
    success_url=reverse_lazy('signin')

class LoginView(FormView):
    form_class=LoginForm
    template_name='login.html'

    def post(self,request, *args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            pwd=form.cleaned_data.get('password')
            usr=authenticate(request,username=username,password=pwd)
            if usr:
                login(request,user=usr)
                return redirect('home')
            else:
                return redirect('signin')

class ChangePasswordView(PasswordChangeView):
    form_class=ChangePassswordForm
    template_name="changepassword.html"
    success_url=reverse_lazy('home')

# class HomeView(ListView):
#     model=Tasks
#     template_name='home.html'
#     context_object_name='tasks'
#     # def form_valid(self, form):
#     #     form.instance.user=self.request.user
#     #     return super().form_valid(form)
#     # def get_context_data(self, **kwargs):
#     #     return super().get_context_data(**kwargs)

def logout_view(request):
    logout(request)
    return redirect('signin')
    
    
    


class HomeView(View):
    def get(self, request, *args, **kwargs):
        form=TaskForm()
        tasks=Tasks.objects.filter(user=request.user,is_active=True).order_by('-created_date')
        return render(request,"home.html",{"form":form,"tasks":tasks})
    
    def post(self, request, *args, **kwargs):
        form=TaskForm(request.POST)
        if form.is_valid():
            user=request.user
            taskname=form.cleaned_data.get("taskname")
            qs=Tasks.objects.create(task=taskname,user=user)
            return redirect('home')
        else:
            return redirect('home')
    
def temp_task_delete_view(request,*args,**kwargs):
    task_id=kwargs.get('id')
    Tasks.objects.filter(id=task_id).update(is_active=False)
    return redirect('home')

def task_delete_view(request,*args,**kwargs):
    task_id=kwargs.get('id')
    task=Tasks.objects.get(id=task_id)
    task.delete()
    return redirect('removedtasks')

def check_task_view(request,*args, **kwargs):
    task_id=kwargs.get('id')
    Tasks.objects.filter(id=task_id).update(checked=True) 
    return redirect('home')

def uncheck_task_view(request,*args, **kwargs):
    task_id=kwargs.get('id')
    Tasks.objects.filter(id=task_id).update(checked=False) 
    return redirect('home')

def get_all_removed_tasks(request,*args, **kwargs):
    user = request.user
    task = Tasks.objects.filter(user = user,is_active=False) 
    return render(request,"unactivetasks.html",{"tasks":task})
