from django.urls import path, include, re_path
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.run, name='run'),
    path('results', views.results, name='results'),
    #path('results/<int:pk>', views.QueryDetailView.as_view(), name='query-detail'),
    path('results/<int:pk>', views.EvidenceUpdateView.as_view(), name='evidence-update'),
    path('results/<gene_id>', views.GeneDetailView.as_view(), name='gene-detail'),
    re_path(r'^run-sh/$', views.run, name='run_sh'),
]
