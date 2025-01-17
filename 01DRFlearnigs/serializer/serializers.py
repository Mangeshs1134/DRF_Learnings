from rest_framework import serializers

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    roll_no = serializers.IntegerField()
    address = serializers.CharField(max_length=70)
    # we must have to create id , unlike auto-generation in models
    id = serializers.IntegerField() 