from rest_framework import serializers
from messages_api.models import Messages
from messages_api.tasks import sent_task


class MessageDetailSerializer(serializers.ModelSerializer):
    """ Сериализатор сообщения """

    def create(self, validated_data):
        """
            Получаем pk, чтобы передать в таску

        :param validated_data:
        :return:
        """
        instance = super().create(validated_data)

        # Ставим задачу отметить как отправдено
        sent_task.delay(instance.pk)
        return instance

    class Meta:
        model = Messages
        fields = '__all__'


class MessageListSerializer(serializers.ModelSerializer):
    """ Сериализатор списка сообщений """

    class Meta:
        model = Messages
        fields = ['id', 'title', 'updated_at']
