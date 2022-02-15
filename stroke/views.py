from rest_framework import generics  # <- import generics
from .models import Questionnaire, Data# <- don't forget your models
from .serializers import QuestionnaireSerializer, DataSerializer # <- or serializers
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly


class QuestionnaireList(generics.ListCreateAPIView):
    queryset = Questionnaire.objects.all()
    serializer_class = QuestionnaireSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    
  # overwrite create method
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class QuestionnaireDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Questionnaire.objects.all()
    serializer_class = QuestionnaireSerializer
    permission_classes = [IsOwnerOrReadOnly]

class DataList(generics.ListCreateAPIView):
    queryset = Data.objects.all()
    serializer_class = DataSerializer
    permission_classes = [permissions.AllowAny]

    



class DataDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Data.objects.all()
    serializer_class = DataSerializer
    permission_classes = [permissions.AllowAny]
