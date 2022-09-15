from rest_framework import views
from rest_framework.response import Response
from hospitalApp.serializers.psaludSerializer import PsaludSerializer

class PsaludViews(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = PsaludSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"mensaje": "Personal de la salud creado"})
