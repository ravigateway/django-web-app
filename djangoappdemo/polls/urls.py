from django.urls import path

from . import views
from . import apiviews

app_name = "polls"

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('blog/', views.blog, name='blog'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('api/questions/', apiviews.questions_view, name='questions_view'),
    path('api/questions/<int:question_id>/', apiviews.question_detail_view, name='question_detail_view'),
    path('api/questions/<int:question_id>/choices/', apiviews.choices_view, name='choices_view'),
    path('api/questions/<int:question_id>/vote/', apiviews.vote_view, name='vote_view'),
    path('api/questions/<int:question_id>/result/', apiviews.question_result_view, name='question_result_view'),
]
