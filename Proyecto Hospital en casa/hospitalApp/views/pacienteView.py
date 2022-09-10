from rest_framework import views
from rest_framework.response import Response
from hospitalApp.serializers.pacienteSerializer import PacienteSerializer

class PacienteViews(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = PacienteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"mensaje": "Paciente creado"})
