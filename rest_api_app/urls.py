from django.urls import path,re_path
from . import views

urlpatterns = [
    re_path('api/$',views.Techie_data.as_view()),
    re_path(r'^api/(?P<id>\d+)/$',views.Techie_data_id.as_view()),
    re_path(r'^api_update_delete/(?P<id>\d+)/$',views.Techie_update_id.as_view()),
]
