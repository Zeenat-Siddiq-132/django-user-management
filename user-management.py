#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests
r = requests.get('url', auth=('user', 'pass'))
r.status_code


# In[ ]:


from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

class CreateUserTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.payload = {
            'username': 'testuser',
            'password': 'testpassword',
            'email': 'testuser@example.com'
        }

    def test_create_user(self):
        response = self.client.post('/api/register/', data=self.payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['username'], self.payload['username'])
        self.assertEqual(response.data['email'], self.payload['email'])


# In[ ]:


INSTALLED_APPS = [
    # ...
    'user_management',
    # ...
]


# In[ ]:


from django.contrib.auth.models import AbstractUser
from user_management.mixins import UserMixin

class User(UserMixin, AbstractUser):
    pass


# In[ ]:


from django.contrib.auth.models import AbstractUser
from user_management.mixins import UserMixin

class User(UserMixin, AbstractUser):
    pass


# In[ ]:


from rest_framework import serializers
from user_management.serializers import UserSerializerMixin

class UserSerializer(UserSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


# In[ ]:


from user_management.views import (
    AuthViewSet,
    PasswordResetViewSet,
    ProfileViewSet,
    RegisterViewSet,
    UsersViewSet,
)
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'auth', AuthViewSet, basename='auth')
router.register(r'password-reset', PasswordResetViewSet, basename='password-reset')
router.register(r'profile', ProfileViewSet, basename='profile')
router.register(r'register', RegisterViewSet, basename='register')
router.register(r'users', UsersViewSet, basename='users')


# In[ ]:


from django.urls import path, include

urlpatterns = [
    # ...
    path('api/', include(router.urls)),
    # ...
]


# In[ ]:


get_ipython().system('pip install django')


# In[ ]:


from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from user_management.serializers import UserSerializer

class AuthView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        refresh = RefreshToken.for_user(request.user)

        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })

class UserListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer


# In[ ]:





# In[ ]:




