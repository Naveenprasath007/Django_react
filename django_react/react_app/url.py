from rest_framework import routers
from .api import UserViewset

routers = routers.DefaultRouter()
routers.register('user',UserViewset,'user')

urlpatterns = routers.urls