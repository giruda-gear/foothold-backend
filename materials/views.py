from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import HttpResponse

from materials.serializers import MeterialSerializer
from materials.models import Material


def index(request):
    return HttpResponse("Welcome! Materials for English Journey.")


@api_view(["GET"])
def get_materials(request):
    queryset = Material.objects.all()
    serializer = MeterialSerializer(queryset, many=True)
    return Response(serializer.data)
