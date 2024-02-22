from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets

from .serializers import GroupSerializer, UserSerializer, LegoColorSerializer, LegoInventorySetsSerializer
from .models import LegoColors, LegoInventorySets


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class GetLegoColors(viewsets.ModelViewSet):
    queryset = LegoColors.objects.all()
    serializer_class = LegoColorSerializer


class GetLegoInventorySets(viewsets.ModelViewSet):
    queryset = LegoInventorySets.objects.all()
    serializer_class = LegoInventorySetsSerializer
