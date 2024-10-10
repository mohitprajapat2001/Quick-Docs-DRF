from rest_framework import viewsets, permissions, throttling
from quick_docs.serializers import BlogSerializer, UserSerializer
from quick_docs.models import Blog
from django.contrib.auth.models import User


class BlogViewSet(viewsets.ModelViewSet):
    """default viewset for blog model"""

    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsAuthenticated]
    throttle_classes = [throttling.AnonRateThrottle]


class UserViewSet(viewsets.ModelViewSet):
    """default viewset for user model"""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class NewUserViewSet(viewsets.GenericViewSet):
    """New User Generic Viewset"""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
    throttle_classes = [throttling.AnonRateThrottle]
    authentication_classes = []
    lookup_field = "username"
