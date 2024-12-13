from rest_framework import serializers
from app.models import Student 

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

    # def validate(self, obj):
    #     if obj.get('age') < 18:
    #         raise serializers.ValidationError("Failed: Age should be greater than 18")
        
    #     if 'z' in obj.get('name'):
    #         raise serializers.ValidationError("Failed: There should be no 'z' in name")
        
    #     return obj

    def validate_age(self, age):
        if age < 18:
            raise serializers.ValidationError("Failed: Age should be greater than 18")
        
        return age
    
    def validate_name(self, name):
        if 'z' in name:
            raise serializers.ValidationError("Failed: There should be no 'z' in name")
        
        return name

