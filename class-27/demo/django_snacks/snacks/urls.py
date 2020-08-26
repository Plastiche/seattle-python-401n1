from django.urls import path
from .views import HomePageView, SnacksPageView, SnackDetailPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('snacks/', SnacksPageView.as_view(), name='snacks'),
    path('snacks_detail/<int:pk>', SnackDetailPageView.as_view(), name='snack_detail')
]
