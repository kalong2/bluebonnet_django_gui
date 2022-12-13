import os
import sys
import django
import pandas as pd
from django.utils import timezone
from datetime import datetime
import pytz

#sys.path.append("/home/klong/bb_django/bluebonnet/var_analysis")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bluebonnet.settings")
django.setup()
#evidence_df = pd.read_csv(sys.argv[1])
#evidence_array = evidence_df.to_dict(orient="records")
#for entry in

print("START")
from var_analysis.models import Evidence, Query
print(sys.argv[1])
now=datetime.now()
'''
entry = Evidence(
        query_str = Query.objects.get(query_str = sys.argv[1]), 
        condition = sys.argv[2],
        hgvsp = sys.argv[3],
        chrom = sys.argv[4],
        start_end = sys.argv[5],
        locus = sys.argv[6],
    gnomad = sys.argv[7],
    exac = sys.argv[8],
    dbsnp = sys.argv[9],
    clinvar = sys.argv[10],
    splice_sites = sys.argv[11],
    ucsc = sys.argv[12],
    polyphen2 = sys.argv[13],
    cadd = sys.argv[14],
    sift = sys.argv[15],
    provean = sys.argv[16],
    date = sys.argv[17],
    user = sys.argv[18]
)
entry.save()
'''
from datetime import datetime
today = str(datetime.now(pytz.timezone('US/Central')).strftime('%Y-%m-%d'))
print("I AM HERE")
this_query = Query.objects.get(query_str = sys.argv[1])
evi_id = this_query.evidence_set.latest('id').id
this_evidence = Evidence.objects.get(id = evi_id)
print(this_evidence)
print(sys.argv[16])
print(sys.argv[17])
print(sys.argv[18])
Evidence.objects.filter(id = evi_id).update(condition = sys.argv[2],
        hgvsp = sys.argv[3],
        chrom = sys.argv[4],
        start_end = sys.argv[5],
        locus = sys.argv[6],
    gnomad = sys.argv[7],
    exac = sys.argv[8],
    dbsnp = sys.argv[9],
    clinvar = sys.argv[10],
    splice_sites = sys.argv[11],
    ucsc = sys.argv[12],
    polyphen2 = sys.argv[13],
    cadd = sys.argv[14],
    sift = sys.argv[15],
    provean = sys.argv[16],
    date_ran = today,
    user = sys.argv[18]
)
Query.objects.filter(query_str = sys.argv[1]).update(running="")
#this_query.latest_evidence = this_evidence
#this_query.save()
