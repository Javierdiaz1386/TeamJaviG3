from rest_framework import views
from rest_framework.response import Response
from hospitalApp.serializers.pacienteSerializer import PacienteSerializer
from hospitalApp.models.paciente import PacienteModels

class PacienteIndividualDetallesViews(views.APIView):
    
    def get(self, reques, id,*args, **kwargs):
        
        queryset = PacienteModels.objects.filter(id=id)
        serializer_class = PacienteSerializer(queryset, many=True)
        return Response(serializer_class.data)
