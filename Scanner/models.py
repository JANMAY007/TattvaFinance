from django.db import models


class Scanner(models.Model):
    class Meta:
        verbose_name = 'Scanner'
        verbose_name_plural = 'Scanners'

    user_id = models.CharField(max_length=20)
    user_loc = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    object = models.manager

    def __str__(self):
        return f'{self.user_id} - {self.user_loc} - {self.created_at}'
