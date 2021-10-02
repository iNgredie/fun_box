from rest_framework import serializers


class VisitedLinksSerializer(serializers.Serializer):
    links = serializers.ListField(child=serializers.CharField())