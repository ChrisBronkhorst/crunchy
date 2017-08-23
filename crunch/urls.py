from django.conf.urls import url, include
from django.views.generic import TemplateView
from rest_framework import routers
from crunch.api.users import UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)


urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='crunch/home.html'), name='home'),
    url(r'api/', include(router.urls))
]

