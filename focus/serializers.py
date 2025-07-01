from rest_framework import serializers
from .models import Session

class SessionSerializer(serializers.ModelSerializer):
    duration = serializers.SerializerMethodField()
    user = serializers.StringRelatedField(read_only=True) # Show user name

    class Meta:
        model = Session
        fields = [
            'id',
            'user',
            'start_time',
            'end_time',
            'expected_duration',
            'was_successful',
            'duration',
        ]
        read_only_fields = ['id', 'start_time', 'user', 'duration']

    def get_duration(self, obj):
        return obj.duration() if obj.end_time else None