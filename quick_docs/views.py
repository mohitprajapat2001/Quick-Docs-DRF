from rest_framework import viewsets, permissions
from quick_docs.serializers import BlogSerializer
from quick_docs.models import Blog


class BlogViewSet(viewsets.ModelViewSet):
    """default viewset for blog model"""

    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [permissions.AllowAny]
