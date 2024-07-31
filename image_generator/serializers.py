from rest_framework import serializers
from .models import TestUser

class TestUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestUser
        fields = '__all__'

class GenerateImageSerializer(serializers.Serializer):
    num_images = serializers.IntegerField(min_value=1)
    prompts = serializers.ListField(
        child=serializers.CharField(max_length=255),
        min_length=1
    )

    def validate(self, data):
        num_images = data['num_images']
        prompts = data['prompts']
        if len(prompts) != num_images:
            raise serializers.ValidationError("Number of prompts must match the number of images.")
        return data
