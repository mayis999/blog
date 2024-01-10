from django.urls import path

from .views.project_views import ProjectDetailGenericView, ProjectListGenericView
from .views.refback_views import RefbackListGenericView
from .views.insurance_views import InsuranceListGenericView

urlpatterns = [  # get: list; post: create
    path('projects/', ProjectListGenericView.as_view()),
    path('projects/<str:pk>/', ProjectDetailGenericView.as_view()),
    path('refback/', RefbackListGenericView.as_view()),
    path('insurance/', InsuranceListGenericView.as_view()),
]




