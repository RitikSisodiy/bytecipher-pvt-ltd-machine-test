from rest_framework import generics
from .serializers import ProductSerializer
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import Product,Image
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework_simplejwt.authentication import JWTAuthentication
class MyPagination(PageNumberPagination):
    page_size = 10

class AddProductView(generics.ListCreateAPIView):
    # permission_classes = [AllowAny]
    authentication_class = JWTAuthentication
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    pagination_class = MyPagination
    permission_classes = [IsAuthenticated]
    # to upload multiple images
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        product = serializer.save()
        images = request.FILES.getlist('images')
        for image in images:
            Image.objects.create(product=product, image=image)
        return Response(serializer.data)
class EditProductView(generics.RetrieveUpdateDestroyAPIView):
    authentication_class = JWTAuthentication
    permission_classes = [IsAuthenticated]
    pagination_class = MyPagination
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

class SearchProductView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.all()
        keywords = self.request.query_params.get('q', None)
        if keywords:
            queryset = queryset.filter(name__contains=keywords)
        return queryset