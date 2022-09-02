from rest_framework.response import Response
from rest_framework.views import APIView
from hospitalApp.models import User
from hospitalApp.api.serializers import userSerializer

class UserApiView(APIView):
    def get(self, request):
        user = User.objects.all()
        user_serialize = userSerializer(user, many=True)
        return Response(
            user_serialize.data
        )