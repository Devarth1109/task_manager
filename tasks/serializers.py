from rest_framework import serializers
from .models import Task
from datetime import date

class TaskSerializer(serializers.ModelSerializer):
    def validate_title(self, value):
        if not value.strip():
            raise serializers.ValidationError("Title cannot be empty or whitespace.")
        return value
    
    def validate_due_date(self, value):
        if value and value < date.today():
            raise serializers.ValidationError("Due date cannot be in the past.")
        return value
    
    def validate(self, data):
        priority = data.get('priority')
        status = data.get('status')
        
        if priority not in ['low', 'medium', 'high']:
            raise serializers.ValidationError({'priority': "Invalid priority value."})
        
        if status not in ['pending', 'completed']:
            raise serializers.ValidationError({'status': "Invalid status value."})
        return data
    
    class Meta:
        model = Task
        fields = '__all__'