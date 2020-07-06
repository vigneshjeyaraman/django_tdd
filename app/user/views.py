from rest_framework import generics
# With ObtainAuthToken we can authenticate user with
# username and password but as we are using email we
# to inherit it and modify
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from user.serializers import UserSerializer, AuthTokenSerializer


class CreateUserView(generics.CreateAPIView):
    """Creates a new user in the system"""
    serializer_class = UserSerializer


class CreateTokenView(ObtainAuthToken):
    """Create a new auth token for user"""
    serializer_class = AuthTokenSerializer
    # renderer classes are used so that we can login using browser
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
