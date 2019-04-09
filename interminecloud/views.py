from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.generics import RetrieveUpdateDestroyAPIView ,RetrieveAPIView ,ListAPIView
from django.contrib.auth.models import User

from .models import UserProfile,IntermineCloud
from interminecloud.serializers import UserProfileSerializer,IntermineSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly ,IsAdminUser,AllowAny


# from .authentication import ExampleAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate, get_user_model
from rest_framework.views import APIView
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework import authentication
from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)



class AuthenticateIntermine(viewsets.ModelViewSet):

    def authenticateintermine(self, request):
        # Get the username and password
        username = request.data.get('username', None)
        password = request.data.get('password', None)

        if not username or not password:
            raise exceptions.AuthenticationFailed(_('No credentials provided.'))

        credentials = {
            get_user_model().USERNAME_FIELD: username,
            'password': password
        }
        user = authenticate(**credentials)

        if user is None:
            raise exceptions.AuthenticationFailed(_('Invalid username/password.'))

        if not user.is_active:
            raise exceptions.AuthenticationFailed(_('User inactive or deleted.'))

        refresh = RefreshToken.for_user(user)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'type':str(1)
        }


class UserprofileViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    http_method_names = ['get', 'post','destroy','patch','head', 'options']
    lookup_field = 'id'



    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({"Success": "User Created.Thanks for registering with us"}, status=status.HTTP_201_CREATED, headers=headers)



class IntermineViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    queryset = IntermineCloud.objects.all()
    serializer_class = IntermineSerializer
    http_method_names = ['get', 'post','destroy','patch','head', 'options']
    lookup_field = 'id'