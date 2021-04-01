from django.conf.urls import url

from . import views

urlpatterns = [

    url('^test_jsonresponse/',views.test_jsonresponse),
    url('^register/',views.register),
    url('^login/',views.login),
    url('^after_login/',views.after_longin),
    url('^logout/',views.logout),
    url('^after_logout/', views.after_logout),
    url('^modify_pwd/', views.modify_pwd ),
    url(r'^', views.index),


]