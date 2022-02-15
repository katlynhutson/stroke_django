from rest_framework import serializers
from .models import Questionnaire, Data

# Reviews


class QuestionnaireSerializer(serializers.HyperlinkedModelSerializer):

    
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Questionnaire
        fields = ('facial_droop', 'arm_drift', 'speech',
                  'owner', 'created_at', 'onset_time', 'additional_notes', 'id')

class DataSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Data
        fields = ('facial_droop', 'arm_drift', 'speech', 'created_at', 'onset_time', 'additional_notes', 'id')