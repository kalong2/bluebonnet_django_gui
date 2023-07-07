from django.views.generic import TemplateView
from django.shortcuts import HttpResponse
from django.template import loader
from django.shortcuts import redirect, render
from django.contrib import messages
import subprocess
from django.forms import formset_factory
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.forms.widgets import Select
import os
from datetime import datetime
import glob
from .models import Query, Evidence, Gene
from .forms import QueryForm, EvidenceForm
from django.utils.safestring import mark_safe
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.utils import timezone
from django.urls import reverse
from datetime import datetime
import pytz
from django.forms.widgets import Select

def run(request):
    context = {}
    QueryFormSet = formset_factory(QueryForm, extra=0)
    formset = QueryFormSet(request.POST)
    if formset.is_valid():
        for form in formset:
            if form.is_valid():
                if form.cleaned_data != {}:
                    cd = form.cleaned_data
                    gene = cd.get('gene')
                    var = cd.get('var')
                    now = datetime.now()
                    date_fmt = now.strftime("%d%b%Y")
                    today = datetime.now(pytz.timezone('US/Central')).strftime('%Y-%m-%d %H:%M:%S')
            #file_prefix = gene + "_" + str(request.user) + "_" + date_fmt
            #print(file_prefix)
            #outfile = open("/home/klong/blah.txt", 'w')
            #subprocess.run(['echo', gene, var], check=True, text=True, stdout=outfile)
                    if gene == "" or var == "":
                        continue
                    else:
                        obj = form.save(commit=False)
                        obj.user_created = request.user
                        obj.user_updated = str(request.user)
                        obj.date_updated = today
                        obj.query_str = str(gene) + ":" + str(var)
                        obj.running = "True"
                        obj.save()
                        if obj.id == None:
                            print("Updating record...")
                        else:
                            obj.analysis()
        messages.add_message(request,
        messages.SUCCESS,
        mark_safe('Variants have been added to the queue<br/>Please check back later for results'))
        return redirect ('/var_analysis')
    else:
        formset = QueryFormSet(initial=[{'gene': '','var': ''}])
    #context['form']= form
    #return render(request, 'var_analysis/run.html', context)
    return render(request, 'var_analysis/run.html', {'formset':formset})
    #return redirect ('/var_analysis')

def results(request):
    context = {'querys': Query.objects.all()}
    return render(request, 'var_analysis/results.html', context)


class QueryDetailView(DetailView):
    model = Query

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
    
class EvidenceUpdateView(UpdateView):
    model = Evidence
    #fields = '__all__'
    fields = ['active_sites' ,'additional_info' ,'reviewer_1' ,'reviewer_2' ,'reviewer_3' ,'gnomad_evidence_category_1' ,'gnomad_evidence_category_2' ,'gnomad_evidence_category_3' ,'gnomad_comment','dbsnp_patho_1' ,'dbsnp_patho_2' ,'dbsnp_patho_3' ,'dbsnp_comment' ,'clinvar_patho_1' ,'clinvar_patho_2' ,'clinvar_patho_3' ,'clinvar_comment' ,'splice_evidence_category_1' ,'splice_evidence_category_2' ,'splice_evidence_category_3' ,'splice_comment' ,'comp_evidence_category_1' ,'comp_evidence_category_2' ,'comp_evidence_category_3' ,'comp_comment' ,'active_sites_evidence_category_1' ,'active_sites_evidence_category_2' ,'active_sites_evidence_category_3' ,'active_sites_comment' ,'additional_evidence_category_1' ,'additional_evidence_category_2' ,'additional_evidence_category_3' ,'additional_comment', 'reviewer_1_patho', 'reviewer_1_evidence', 'reviewer_2_patho', 'reviewer_2_evidence', 'reviewer_3_patho', 'reviewer_3_evidence']
    #success_url ="/"

    def get_success_url(self):
        pk = self.kwargs["pk"]
        # No need for reverse_lazy here, because it's called inside the method
        return reverse('evidence-update', kwargs={"pk":pk})

class GeneDetailView(DetailView):
    model = Gene
    slug_field = "gene_id"
    slug_url_kwarg = 'gene_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context



#class query_view(request, slug):
    #query_view = get_object_or_404(query, slug=slug)
    #return render(request, 'var_analysis/query_view.html', {'query_view' : query_view})


