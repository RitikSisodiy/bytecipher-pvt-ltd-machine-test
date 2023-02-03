from django.shortcuts import render
from rest_framework import generics
from .serializers import UserSerializer,LoginSerializer
from rest_framework.response import Response
from rest_framework.authentication import authenticate
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
# Create your views here.

class UserCreate(generics.CreateAPIView):
    serializer_class = UserSerializer

class LoginView(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        email = request.data.get("email", "")
        password = request.data.get("password", "")
        user = authenticate(request, username=email, password=password)
        if user is not None:
            if user.is_active:
                refresh = RefreshToken.for_user(user)
                return Response({
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                })
            else:
                return Response({"error": "User is not active."}, status=400)
        else:
            return Response({"error": "Invalid credentials."}, status=400)