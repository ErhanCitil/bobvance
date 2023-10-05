from django.urls import path, include
from bobvance.base.views import Home

urlpatterns = [
    path('', Home.as_view(), name='home')
]
