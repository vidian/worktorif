from rest_framework import serializers
from .models import Company

class CompanySerializers(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['company_name', 'company_registration_number', 'portal_url', 'phone_number', 'address']

    def create(self, validated_data):
        print(validated_data)
        return Company.objects.create(**validated_data)