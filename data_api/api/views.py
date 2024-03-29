from django.contrib.auth.models import Group, User
from django.db.models import Sum
from rest_framework import permissions, viewsets

from .serializers import GroupSerializer, UserSerializer, LegoColorSerializer, LegoInventorySetsSerializer, \
    LegoSetsSerializer, LegoPartsPerYearSerializer
from .models import LegoColors, LegoInventorySets, LegoSets


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
    print(queryset)
    serializer_class = LegoColorSerializer


class GetLegoInventorySets(viewsets.ModelViewSet):
    queryset = LegoInventorySets.objects.all()
    serializer_class = LegoInventorySetsSerializer


class GetLegoPartsPerYear(viewsets.ModelViewSet):
    # queryset = LegoSets.objects.raw("select max(set_num), year, sum(num_parts) from lego_sets group by year order by year limit 10;")
    queryset = LegoSets.objects.values("year").annotate(total_parts=Sum('num_parts'))

    print(queryset)
    serializer_class = LegoPartsPerYearSerializer
