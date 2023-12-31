from django.db import models
from mypage.models import Receiver
from rest_framework import serializers

# Create your models here.

class Message(models.Model):
    CATEGORY_CHOICES = [
        ('today', 'Today'),
        ('simple', 'Simple'),
        ('special', 'Special'),
        ('cute', 'Cute'),
    ]

    category = models.CharField(
        max_length=10,
        choices=CATEGORY_CHOICES,
        default='today',
        verbose_name='카테고리'
    )
    
    content = models.TextField(verbose_name='내용')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='작성일')
    is_recommended = models.BooleanField(default=False, verbose_name='추천 여부')


    def __str__(self):
        return f'{self.category} - {self.content} ({self.created_at})'