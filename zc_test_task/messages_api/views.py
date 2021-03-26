from rest_framework import mixins, generics, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from rest_framework.views import APIView

from messages_api.serializers import *


class MessageCreateView(mixins.CreateModelMixin, generics.GenericAPIView):
    """ Создание сообщения """

    serializer_class = MessageDetailSerializer

    # Ограничим количество запросов для всех юзеров
    throttle_classes = [UserRateThrottle, AnonRateThrottle]

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


class MessageReadView(APIView):
    """
    Помечаем сообщение прочитанным

    """

    def patch(self, request, pk):
        message_obj = get_object_or_404(Messages, pk=pk)

        serializer = MessageDetailSerializer(message_obj, data={'read': True}, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
