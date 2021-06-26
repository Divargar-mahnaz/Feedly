from rest_framework import serializers

from Feedly.settings import BASE_URL
from ..models import Feed


class UserFeedsSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    image = serializers.SerializerMethodField()

    class Meta:
        model = Feed
        fields = ('id', 'name', 'link', 'image')

    @staticmethod
    def get_image(obj):
        return BASE_URL + obj.image.url
