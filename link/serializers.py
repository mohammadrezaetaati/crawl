from rest_framework import serializers


class AddUrlSerializers(serializers.Serializer):
    url = serializers.CharField()
