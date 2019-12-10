from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from api import views


router = DefaultRouter()
router.register(r'product', views.ProductView)
# api url 配置
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^test/$', views.GetMessageView.as_view()),
]