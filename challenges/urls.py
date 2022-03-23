from django.urls import path
from . import views
urlpatterns = [
    path("",views.index),
    path("<int:months>",views.Monthly_challenges__number),
    path("<str:months>",views.Monthly_challenges, name="challenges-tushar")
]
