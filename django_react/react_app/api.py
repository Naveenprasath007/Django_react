from react_app.models import user
from rest_framework import viewsets,permissions
from .serializers import userSerializer

class UserViewset(viewsets.ModelViewSet):
    queryset =user.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = userSerializer