from django.db import models

class Message(models.Model):
    """
        메시지 DB
    """
    sentence = models.CharField("Sentence", max_length=80)
    depth = models.PositiveIntegerField()
    link = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Message DB'
        db_table = 'messages'

    
