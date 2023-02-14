from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.template import loader
from django.views.generic import TemplateView
#from django.apps import var_analysis
from var_analysis.models import Query, Evidence
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect


#def home(request):
#    context = {}
#    return render(request, 'home.html', context)

class MultipleModelView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
         context = super(MultipleModelView, self).get_context_data(**kwargs)
         context['Query'] = Query.objects.all()
         context['Evidence'] = Evidence.objects.all()
         return context

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Your password has been changed")
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error')

    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {'form': form})
