from rest_framework import serializers
from .models import Lead

class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = ('id', 'phone_number', 'name', 'email', 'message')

    def to_representation(self, data):
        return {
            'id': data.id,
            'phone-number': data.phone_number,
            'name': data.name,
            'email': data.email,
            'message': data.message,
        }

    def to_internal_value(self, data):
        return {
            'phone_number': data.get('phone-number'),
            'name': data.get('name'),
            'email': data.get('email'),
            'message': data.get('message')
        }