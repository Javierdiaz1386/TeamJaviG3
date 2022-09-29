from rest_framework import views
from rest_framework.response import Response
from hospitalApp.serializers.usuarioSerializers import UsuarioSerializer
from hospitalApp.models.usuario import UsuarioModel

class UsersDetallesViews(views.APIView):
    
    def get(self, reques, *args, **kwargs):
        
        queryset = UsuarioModel.objects.all()
        serializer_class = UsuarioSerializer(queryset, many=True)
        return Response(serializer_class.data)
