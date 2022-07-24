from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import AddUrlSerializers
from .tasks import crawl


class Crawl(APIView):
    def post(self, request):
        crawl.delay("namasha_com.csv")
        return Response(status=status.HTTP_200_OK)


class AddUrl(APIView):
    def get(self, request):
        serializers = AddUrlSerializers(data=request.data)
        if serializers.is_valid():
            url = serializers.validated_data.get("url")
            with open("namasha_com", "a") as f:
                f.write(f"{url}\n")
            return Response(status=200)
        return Response(status=status.HTTP_404_NOT_FOUND)
