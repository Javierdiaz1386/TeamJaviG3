from rest_framework import views
from rest_framework.response import Response
from hospitalApp.serializers.pacienteSerializer import PacienteSerializer
from hospitalApp.models.paciente import PacienteModels

class PacienteDetallesViews(views.APIView):
    
    def get(self, reques, *args, **kwargs):
        
        queryset = PacienteModels.objects.all()
        serializer_class = PacienteSerializer(queryset, many=True)
        return Response(serializer_class.data)
