from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer


# Custom permission: Only admins can modify data; others read-only
class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_authenticated and request.user.is_staff)


# Category ViewSet
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['name']


# Product ViewSet
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.select_related('category', 'created_by').all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminOrReadOnly]

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = {
        'category__name': ['exact'],
        'price': ['gte', 'lte'],
        'stock': ['gte', 'lte'],
    }
    search_fields = ['name', 'description', 'category__name']
    ordering_fields = ['price', 'created_at', 'stock']

    def perform_create(self, serializer):
        # Automatically set the creator if authenticated
        user = self.request.user if self.request.user.is_authenticated else None
        serializer.save(created_by=user)
