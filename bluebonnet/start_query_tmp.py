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

from var_analysis.models import Evidence, Query
name=sys.argv[1] + ":" + sys.argv[2]
from datetime import datetime
today = str(datetime.now(pytz.timezone('US/Central')).strftime('%Y-%m-%d'))
print(name)
entry = Evidence(
        query_str = Query.objects.get(query_str = name),
        condition = "tmp",
        hgvsp = "tmp",
        chrom = "tmp",
        start_end = "tmp",
        locus = "tmp",
    gnomad = "tmp",
    exac = "tmp",
    dbsnp = "tmp",
    clinvar = "tmp",
    splice_sites = "tmp",
    ucsc = "tmp",
    polyphen2 = "tmp",
    cadd = "tmp",
    sift = "tmp",
    provean = "tmp",
    date_ran = today,
    user = "tmp"
)
entry.save()
this_query = Query.objects.get(query_str = name)
evi_id = this_query.evidence_set.latest('id').id
this_evidence = Evidence.objects.get(id = evi_id)
Query.objects.filter(query_str = name).update(running="True", latest_evidence=this_evidence)
#this_query.latest_evidence = this_evidence
#this_query.save()
