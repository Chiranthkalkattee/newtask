from .models import Candidate_details,skill_details
from rest_framework import serializers


class CandidateSerializer(serializers.ModelSerializer):
    skill = serializers.StringRelatedField(many=True)
    class Meta:
        model = Candidate_details
        fields = ['name','age','gender','skills','skill']
