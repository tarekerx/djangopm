from django.shortcuts import render,redirect
from django.views.generic import CreateView
from .forms import userregistrationform,Profile_Form
from django.urls import reverse_lazy
# Create your views here.
from django.contrib.auth  import login
from django.contrib.auth.decorators import login_required

class registerview(CreateView):
    form_class = userregistrationform
    # success_url = reverse_lazy("login")
    template_name = "registration/register.html"
    def get_success_url(self):
        login(self.request, self.object)
        return reverse_lazy('project_list')
    
    
    
@login_required
def edit_profile(req):
    if req.method == "POST":
        form = Profile_Form(req.POST,instance = req.user)
        if form.is_valid():
            form.save()
            return redirect("profile")
        
    else:
            
        form = Profile_Form(instance = req.user)
        
        return render(req,"registration/profile.html",{
            "form":form
        })
    