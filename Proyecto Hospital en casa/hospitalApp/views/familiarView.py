from rest_framework import views
from rest_framework.response import Response
from hospitalApp.serializers.familiarSerializer import FamiliarSerializer

class FamiliarViews(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = FamiliarSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"mensaje": "Familiar  creado"})
