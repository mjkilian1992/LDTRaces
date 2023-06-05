from django.urls import path

from races import views as races_views

urlpatterns = [
    path('tickets/', races_views.ListCreateTickets.as_view(), name='tickets')
]