from django.conf.urls import url, include
from django.views.generic import TemplateView
from rest_framework import routers
from crunch.api.users import UserViewSet
from crunch.api.companies import CompanyViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'companies', CompanyViewSet)


urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='crunch/home.html'), name='home'),
    url(r'api/', include(router.urls))
]

