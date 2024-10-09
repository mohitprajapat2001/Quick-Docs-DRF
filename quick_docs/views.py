from rest_framework import viewsets, permissions
from quick_docs.serializers import BlogSerializer, UserSerializer
from quick_docs.models import Blog
from django.contrib.auth.models import User


class BlogViewSet(viewsets.ModelViewSet):
    """default viewset for blog model"""

    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = "slug"


class UserViewSet(viewsets.ModelViewSet):
    """default viewset for user model"""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
