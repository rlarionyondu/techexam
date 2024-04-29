from django.urls import path
from . import views

urlpatterns = [
    path('region/', views.RegionViewSet.as_view()),
    path('region/<int:id>/', views.RegionUpdateViewSet.as_view()),
    path('province/', views.ProvinceViewSet.as_view()),
    path('province/<int:id>/', views.ProvinceUpdateViewSet.as_view()),
]
