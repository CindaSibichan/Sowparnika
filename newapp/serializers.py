# serializers.py
from rest_framework import serializers
from .models import UsersModel

class ContactSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsersModel
        fields = ['name', 'phone', 'email']
