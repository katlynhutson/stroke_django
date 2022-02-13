from rest_framework import serializers
from .models import Questionnaire

# Reviews


class QuestionnaireSerializer(serializers.HyperlinkedModelSerializer):

    # how to populate the owner field on review data
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Questionnaire
        fields = ('facial_droop', 'arm_drift', 'speech',
                  'owner', 'created_at', 'onset_time', 'additional_notes', 'id')
