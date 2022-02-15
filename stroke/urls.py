from django.urls import path, include

from . import views

urlpatterns = [
    path('questionnaires/', views.QuestionnaireList.as_view(), name='questionnaires_list'),
    path('questionnaires/<int:pk>',
         views.QuestionnaireDetail.as_view(), name='questionnaires_detail'),
    path('data/', views.DataList.as_view(), name='data_list'),
    path('data/<int:pk>', views.DataDetail.as_view(), name='data_detail'),
   
]