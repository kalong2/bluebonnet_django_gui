from django import forms

from .models import Query, Evidence

class QueryForm(forms.ModelForm):
    class Meta:
        model = Query
        fields = '__all__'

class EvidenceForm(forms.ModelForm):
    class Meta:
        model = Evidence
        fields = '__all__'

