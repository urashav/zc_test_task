from rest_framework import serializers
from messages_api.models import Messages


class MessageDetailSerializer(serializers.ModelSerializer):
    """ Сериализатор сообщения """

    class Meta:
        model = Messages
        fields = '__all__'


class MessageListSerializer(serializers.ModelSerializer):
    """ Сериализатор списка сообщений """

    class Meta:
        model = Messages
        fields = ['id', 'title', 'updated_at']
