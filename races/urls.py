from django.urls import path

from races import views as races_views

urlpatterns = [
    path('races/', races_views.ListRaceStarts.as_view())
]