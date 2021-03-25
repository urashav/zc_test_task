from rest_framework import mixins, generics
from messages_api.serializers import *


class MessageCreateView(mixins.CreateModelMixin, generics.GenericAPIView):
    """ Создание сообщения """

    serializer_class = MessageDetailSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class MessageListView(generics.ListAPIView):
    """ Список сообщений """

    serializer_class = MessageListSerializer
    queryset = Messages.objects.all()


class MessageDetailView(generics.RetrieveDestroyAPIView):
    """Просмотр/удаление сообщения """

    serializer_class = MessageDetailSerializer
    queryset = Messages.objects.all()
