from rest_framework.views import APIView
from rest_framework.response import Response

from races import api as races_api


class ListRaceStarts(APIView):

    def get(self, request, *args, **kwargs):
        return Response(races_api.load_race_data())
