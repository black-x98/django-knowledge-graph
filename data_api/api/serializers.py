from django.contrib.auth.models import Group, User
from .models import LegoColors, LegoInventorySets, LegoSets, LegoPartsPerYear
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class LegoColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = LegoColors
        fields = "__all__"


class LegoInventorySetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LegoInventorySets
        fields = "__all__"


class LegoSetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LegoSets
        fields = "__all__"


class LegoPartsPerYearSerializer(serializers.ModelSerializer):
    class Meta:
        model = LegoPartsPerYear
        fields = "__all__"