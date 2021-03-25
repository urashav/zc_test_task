from django.db import models


class Messages(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=250, null=False)
    message = models.TextField(verbose_name='Текст', null=False)
    read = models.BooleanField(verbose_name='Прочитано', null=False, default=False)
    sent = models.BooleanField(verbose_name='Отправлено', null=False, default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
