from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from .serializers import RegisterSerializer, UserSerializer
from django.contrib.auth import get_user_model
from rest_framework import status, permissions, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import User
from .serializers import UserSerializer

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        user = User.objects.get(username=response.data['username'])
        token, created = Token.objects.get_or_create(user=user)
        return Response({"user": response.data, "token": token.key})

class LoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key})
        return Response({"error": "Invalid Credentials"}, status=400)

class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user




class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=["post"])
    def follow(self, request, pk=None):
        user_to_follow = get_object_or_404(User, pk=pk)
        request.user.follow(user_to_follow)
        return Response({"message": f"You are now following {user_to_follow.username}"}, status=status.HTTP_200_OK)

    @action(detail=True, methods=["post"])
    def unfollow(self, request, pk=None):
        user_to_unfollow = get_object_or_404(User, pk=pk)
        request.user.unfollow(user_to_unfollow)
        return Response({"message": f"You unfollowed {user_to_unfollow.username}"}, status=status.HTTP_200_OK)
