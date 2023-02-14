from django.db import models
from django.contrib.auth.models import User
import datetime
import subprocess
from django.forms import ModelChoiceField
from datetime import datetime
import pytz

class Query(models.Model):
    #GENE_CHOICES =(
    #("ABCD1", "ABCD1"),
    #("ACADVL", "ACADVL"),
    #("HBB", "HBB"),)
    #gene = models.CharField(max_length=25,choices=GENE_CHOICES)
    gene = models.ForeignKey('Gene', on_delete=models.DO_NOTHING)
    var = models.CharField(max_length=25, default='')
    query_str = models.CharField(max_length=50, default='', editable = False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.CharField(max_length=25, editable = False)
    user_created = models.ForeignKey(User, editable = False, on_delete=models.DO_NOTHING, null=True, blank=True)
    user_updated = models.CharField(max_length=50, editable = False)
    latest_evidence = models.ForeignKey('Evidence', editable = False, on_delete=models.DO_NOTHING, null=True, blank=True)
    running = models.CharField(max_length=50, default='', editable = False, null=True, blank=True)

    #@property
    def __str__(self):
        return "%s:%s" % (self.gene, self.var)

    def save(self,*args,**kwargs):
        query_str_check = Query.objects.filter(query_str=self.query_str)
        if query_str_check: # if some items are found in the database
            query_str_check.update(date_updated=self.date_updated)
            query_str_check.update(user_updated=self.user_updated)
            query_str_check.update(running=self.running)
            #print(query_str_check.first().id)
            qid=list(query_str_check.values_list('id', flat=True))[0]
        else:
            return super(Query,self).save(*args,**kwargs)
        
        query_str_check.first().analysis()

    def analysis(self,*args,**kwargs):
        date_folder = "/work/NBS/outputs/" + str(self.date_updated) + "/"
        query_prefix = str(self.gene) + "_" + str(self.id) + "_" + str(self.user_updated) + "_" + str(self.date_updated)
        input_file = "/work/NBS/inputs/" + query_prefix + ".txt"
        latest_out = "/work/NBS/outputs/latest/" + str(self.gene) + "_" + str(self.id) + "_latest.txt"
        latest_log = "/work/NBS/outputs/latest/" + str(self.gene) + "_" + str(self.id) + "_latest.log"
        rmv_latest = "rm -f /work/NBS/outputs/latest/" + str(self.gene) + "_" + str(self.id) + "*"
        query_input_cmd = "echo '" + str(self.gene) + " " + str(self.var) + "' >|" + input_file
        #print(query_prefix)
        #print(query_input_cmd)
        #subprocess.run(['mkdir', "-p", "/work/NBS/outputs/latest/"], check=True, text=True)
        subprocess.run(['mkdir', "-p", date_folder], check=True, text=True)
        subprocess.call([query_input_cmd], shell=True)
        subprocess.run(['/work/NBS/runNBS.sh',input_file, str(self.date_updated), str(self.user_updated)], check=True, text=True)

class Evidence(models.Model):
    query_str = models.ForeignKey(Query, on_delete=models.CASCADE)
    condition = models.CharField(max_length=50, default='')
    hgvsp = models.CharField(max_length=50, default='', editable=True)
    chrom = models.CharField(max_length=50, default='')
    start_end = models.CharField(max_length=50, default='')
    locus = models.CharField(max_length=50, default='')
    gnomad = models.TextField(max_length=10000, default='')
    exac = models.TextField(max_length=10000, default='')
    dbsnp = models.TextField(max_length=10000, default='')
    clinvar = models.TextField(max_length=10000, default='')
    splice_sites = models.TextField(max_length=10000, default='')
    ucsc = models.CharField(max_length=10000, default='')
    polyphen2 = models.CharField(max_length=10000, default='')
    cadd = models.CharField(max_length=10000, default='')
    sift = models.CharField(max_length=10000, default='')
    provean = models.CharField(max_length=10000, default='')
    active_sites = models.TextField(max_length=10000, null=True, blank=True)
    additional_info = models.TextField(max_length=10000, null=True, blank=True)
    date_ran = models.CharField(max_length=25, editable = False)
    user = models.CharField(max_length=50, editable = False)

    reviewer_1 = models.ForeignKey(User,on_delete=models.DO_NOTHING,related_name='first_reviewer', verbose_name="First Reviewer", blank=True,null=True)  
    reviewer_1_patho = models.CharField(max_length=100, default='', blank=True,null=True)
    reviewer_1_evidence = models.CharField(max_length=100, default='', blank=True,null=True) 
    reviewer_2 = models.ForeignKey(User,on_delete=models.DO_NOTHING,related_name='second_reviewer', verbose_name="Second Reviewer", blank=True,null=True)  
    reviewer_2_patho = models.CharField(max_length=100, default='', blank=True,null=True)
    reviewer_2_evidence = models.CharField(max_length=100, default='', blank=True,null=True)
    reviewer_3 = models.ForeignKey(User,on_delete=models.DO_NOTHING,related_name='third_reviewer', verbose_name="Third Reviewer", blank=True,null=True)  
    reviewer_3_patho = models.CharField(max_length=100, default='', blank=True,null=True)
    reviewer_3_evidence = models.CharField(max_length=100, default='', blank=True,null=True)

    
    gnomad_evidence_category_1 = models.CharField(max_length=50, default='', blank=True,null=True)
    gnomad_evidence_category_2 = models.CharField(max_length=50, default='', blank=True,null=True)
    gnomad_evidence_category_3 = models.CharField(max_length=50, default='', blank=True,null=True)
    gnomad_comment = models.TextField(max_length=10000, default='', blank=True,null=True)
    exac_evidence_category_1 = models.CharField(max_length=50, default='', blank=True,null=True)
    exac_evidence_category_2 = models.CharField(max_length=50, default='', blank=True,null=True)
    exac_evidence_category_3 = models.CharField(max_length=50, default='', blank=True,null=True)
    exac_comment = models.TextField(max_length=10000, default='', blank=True,null=True)
    dbsnp_patho_1 = models.CharField(max_length=50, default='', blank=True,null=True)
    dbsnp_patho_2 = models.CharField(max_length=50, default='', blank=True,null=True)
    dbsnp_patho_3 = models.CharField(max_length=50, default='', blank=True,null=True)
    dbsnp_comment = models.TextField(max_length=10000, default='', blank=True,null=True)
    clinvar_patho_1 = models.CharField(max_length=50, default='', blank=True,null=True)
    clinvar_patho_2 = models.CharField(max_length=50, default='', blank=True,null=True)
    clinvar_patho_3 = models.CharField(max_length=50, default='', blank=True,null=True)
    clinvar_comment = models.TextField(max_length=10000, default='', blank=True,null=True)
    splice_evidence_category_1 = models.CharField(max_length=50, default='', blank=True,null=True)
    splice_evidence_category_2 = models.CharField(max_length=50, default='', blank=True,null=True)
    splice_evidence_category_3 = models.CharField(max_length=50, default='', blank=True,null=True)
    splice_comment = models.TextField(max_length=10000, default='', blank=True,null=True)
    comp_evidence_category_1 = models.CharField(max_length=50, default='', blank=True,null=True)
    comp_evidence_category_2 = models.CharField(max_length=50, default='', blank=True,null=True)
    comp_evidence_category_3 = models.CharField(max_length=50, default='', blank=True,null=True)
    comp_comment = models.TextField(max_length=10000, default='', blank=True,null=True)
    active_sites_evidence_category_1 = models.CharField(max_length=50, default='', blank=True,null=True)
    active_sites_evidence_category_2 = models.CharField(max_length=50, default='', blank=True,null=True)
    active_sites_evidence_category_3 = models.CharField(max_length=50, default='', blank=True,null=True)
    active_sites_comment = models.TextField(max_length=10000, default='', blank=True,null=True)
    additional_evidence_category_1 = models.CharField(max_length=50, default='', blank=True,null=True)
    additional_evidence_category_2 = models.CharField(max_length=50, default='', blank=True,null=True)
    additional_evidence_category_3 = models.CharField(max_length=50, default='', blank=True,null=True) 
    additional_comment = models.TextField(max_length=10000, default='', blank=True,null=True)


    def __str__(self):
        return str(self.id)

class Gene(models.Model):
    gene_id = models.CharField(max_length=50, default='', primary_key = True)
    condition = models.CharField(max_length=50, default='')
    condition_site = models.CharField(max_length=1000, default='', blank=True, null=True)
    chrom = models.CharField(max_length=50, default='')
    start_end = models.CharField(max_length=100, default='')
    locus = models.CharField(max_length=50, default='')
    transcript = models.CharField(max_length=50, default='')
    np_id = models.CharField(max_length=50, default='')
    gnomad_link = models.CharField(max_length=1000, default='')
    ncbi_gene_link = models.CharField(max_length=1000, default='')

    def __str__(self):
        return str(self.gene_id)

class Reviewer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    reviewer_1 = models.BooleanField(default=False)
    reviewer_2 = models.BooleanField(default=False)
    reviewer_3 = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)
