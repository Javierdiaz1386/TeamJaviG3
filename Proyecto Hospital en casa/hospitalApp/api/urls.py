from django.urls import path
from hospitalApp.api.api import UserApiView

urlpatterns = [
    path('usuario/', UserApiView.as_view(), name ='usuario_api')
]
