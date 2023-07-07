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
name=sys.argv[1] + ":" + sys.argv[2]
from datetime import datetime
today = str(datetime.now(pytz.timezone('US/Central')).strftime('%Y-%m-%d'))
entry = Evidence(
        query_str = Query.objects.get(query_str = name),
        condition = "tmp",
        hgvsp = "tmp",
        chrom = "tmp",
        start_end = "tmp",
        locus = "tmp",
    gnomad = "tmp",
    dbsnp = "tmp",
    clinvar = "tmp",
    splice_sites = "tmp",
    ucsc = "tmp",
    polyphen2 = "tmp",
    cadd = "tmp",
    sift = "tmp",
    provean = "tmp",
    date_ran = today,
    user = "tmp",
    rsid = "tmp",
    clinvar_id = "tmp",
    clinvar_interp = "tmp",
    clinvar_date = "tmp",
    clinvar_acc = "tmp",
    pubmed = "tmp",
    google = "tmp",
    pubsearch = "tmp",
    norm_var = "tmp"
)
entry.save()
this_query = Query.objects.get(query_str = name)
evi_id = this_query.evidence_set.latest('id').id
this_evidence = Evidence.objects.get(id = evi_id)
Query.objects.filter(query_str = name).update(running="True", latest_evidence=this_evidence)
