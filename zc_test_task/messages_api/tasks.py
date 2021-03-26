from messages_api.models import Messages
from zc_test_task.celery import app


@app.task
def sent_task(message_pk):
    """
        Таска устанавливает флаг sent(отправлено) сообщению

    :param message_pk: pk созданного сообщения
    :return:
    """
    message = Messages.objects.get(pk=message_pk)
    message.sent = True
    message.save()
