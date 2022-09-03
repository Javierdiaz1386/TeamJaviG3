
from rest_framework.response import Response
from rest_framework.views import APIView
from hospitalApp.models import Pacientes, User
from hospitalApp.api.serializers import PacientesSerializer, userSerializer

class UserApiView(APIView):
    def get(self, request):
        user = User.objects.all()
        user_serialize = userSerializer(user, many=True)
        print(user_serialize.data)
        return Response(
            user_serialize.data
        )

    def post(self,request):
         user_serializer = userSerializer(data = request.data)
         if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data)
         else:
            return Response(user_serializer.errors)

class PacienteApiView(APIView):
    def get(self,request):
        paciente = Pacientes.objects.all()
        paciente_serialize = PacientesSerializer(paciente, many=True)
        print(paciente_serialize.data)
        return Response(paciente_serialize.data)
    def post(self, request):
        paciente_serializer = PacientesSerializer(data = request.data)
        if paciente_serializer.is_valid():
            paciente_serializer.save()
            return Response(paciente_serializer.data)
        else:
            return Response(paciente_serializer.errors)