from django.urls import path

from apps.contests.views import DetailView

app_name = "contests"

urlpatterns = [
    path("<int:pk>/", DetailView.as_view(), name="detail"),
]
