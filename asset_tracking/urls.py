from django.conf.urls import include,url

from . import views
from django.contrib.auth import views as auth_views
from . import forms

urlpatterns = [
    url(r'^home/$', views.asset_list,name='asset_list'),
    url(r'^create/$', views.asset_create,name='asset_create'),
    url(r'^update/(?P<pk>\d+)$',views.asset_update,name='asset_update'),
    url(r'^delete/(?P<pk>\d+)$',views.asset_delete,name='asset_delete'),
    url(r'^$',auth_views.login,{'authentication_form': forms.LoginForm},name='login'),
    url(r'^logout/$',auth_views.logout,{'next_page': 'login'},name='logout'),
    url(r'^hcreate/(?P<pk>\d+)$',views.history_create,name='history_create'),
    url(r'^report/$',views.report,name='report'),
    url(r'^api/data/$',views.ChartData.as_view(),name='api-data'),
    url(r'^pdf/$',views.GeneratePdf.as_view(),name='pdf'),
]
