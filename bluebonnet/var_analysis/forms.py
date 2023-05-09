from django import forms
from django.forms import modelformset_factory
from .models import Query, Evidence

'''
class BaseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BaseForm, self).__init__(*args, **kwargs)
        for bound_field in self:
            if hasattr(bound_field, "field") and bound_field.field.required:
                bound_field.field.widget.attrs["required"] = "required"
'''
class QueryForm(forms.ModelForm):
    #def __init__(self, *args, **kwargs):
        #super(QueryForm, self).__init__(*args, **kwargs)
        #for bound_field in self:
            #print(bound_field)
            #if hasattr(bound_field, "field") and bound_field.field.required:
                #bound_field.field.widget.attrs["required"] = "required"
    
    class Meta:
        model = Query
        fields = '__all__'



class EvidenceForm(forms.ModelForm):
    widgets = {'active_sites': forms.Textarea(attrs={'rows': 100000}),}
    
    class Meta:
        model = Evidence
        fields = '__all__'
