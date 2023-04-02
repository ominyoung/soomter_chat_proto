from django.db import models

class IntroChat(models.Model):
    """
        도입 DB
    """
    sentence =  models.TextField()
    depth = models.IntegerField()
    link = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'IntroChat DB'
        db_table = 'introchat'

    
