from django.conf.urls import url
from django.conf.urls import include


from . import views

urlpatterns = [
    url('Food/', views.FoodAPIView.as_view()),

]
