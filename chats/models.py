# from django.db import models
#
# from accounts.models import User
#
#
# class Chat(models.Model):
#     date = models.DateField('Date')
#     chatter = models.CharField(max_length=80)
#     utterance = models.TextField()
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
#     # created_at = models.DateField(auto_now_add=True)
#
#     class Meta:
#         verbose_name_plural = 'Chat DB'
#         db_table = 'chats'
