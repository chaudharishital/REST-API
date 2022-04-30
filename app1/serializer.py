from rest_framework import serializers

class StudentSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=20)
    roll_no=serializers.IntegerField()
    marks=serializers.IntegerField()
