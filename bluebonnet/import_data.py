import os
import sys
import django
import pandas as pd
from django.utils import timezone
from datetime import datetime
import pytz


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bluebonnet.settings")
django.setup()

from var_analysis.models import Evidence, Query
now=datetime.now()
from datetime import datetime
today = str(datetime.now(pytz.timezone('US/Central')).strftime('%Y-%m-%d'))
print(sys.argv[1])
this_query = Query.objects.get(query_str = sys.argv[1])
evi_id = this_query.evidence_set.latest('id').id
this_evidence = Evidence.objects.get(id = evi_id)
Evidence.objects.filter(id = evi_id).update(condition = sys.argv[2],
        hgvsp = sys.argv[3],
        chrom = sys.argv[4],
        start_end = sys.argv[5],
        locus = sys.argv[6],
    gnomad = sys.argv[7],
    dbsnp = sys.argv[8],
    clinvar = sys.argv[9],
    splice_sites = sys.argv[10],
    ucsc = sys.argv[11],
    polyphen2 = sys.argv[12],
    cadd = sys.argv[13],
    sift = sys.argv[14],
    provean = sys.argv[15],
    date_ran = today,
    user = sys.argv[17],
    rsid = sys.argv[18],
    clinvar_id = sys.argv[19],
    clinvar_interp = sys.argv[20],
    clinvar_date = sys.argv[21],
    clinvar_acc = sys.argv[22],
    pubmed = sys.argv[23],
    google = sys.argv[24],
    pubsearch = sys.argv[25],
    norm_var = sys.argv[26],
)
Query.objects.filter(query_str = sys.argv[1]).update(running="")
