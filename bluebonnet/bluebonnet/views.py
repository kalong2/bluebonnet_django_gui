from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.template import loader
from django.views.generic import TemplateView
#from django.apps import var_analysis
from var_analysis.models import Query, Evidence

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
