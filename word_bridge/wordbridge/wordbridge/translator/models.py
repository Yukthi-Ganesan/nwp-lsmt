from django.db import models

class TranslationHistory(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    text = models.TextField()
    translated_text = models.TextField()
    source_language = models.CharField(max_length=50)
    target_language = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.source_language} to {self.target_language}"

