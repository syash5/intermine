from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile,IntermineCloud
from rest_framework.response import Response
from rest_framework import status

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

    def validate(self, data):
        str = data['username']
        if str.isalpha()==True:
            raise serializers.ValidationError("username Should be more than 6 letters,alphanumeric and first letter should be alphabet")
        elif len(str)<6:
            raise serializers.ValidationError("username Should be more than 6 letters,alphanumeric and first letter should be alphabet")
        elif (str[0]).isalpha() ==  False:
            raise serializers.ValidationError("username Should be more than 6 letters,alphanumeric and first letter should be alphabet")
        if len(data['contact_no']) <10:
            raise serializers.ValidationError("Invalid Contact,Please Enter 10 digit Contact Number")
        return data

class IntermineSerializer(serializers.ModelSerializer):
    class Meta:
        model = IntermineCloud
        fields = '__all__'        