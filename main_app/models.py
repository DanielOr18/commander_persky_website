from django.db import models
from django.utils import timezone

# Create your models here.

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"Message from {self.name} - {self.subject}"

class SiteStatistics(models.Model):
    site_visits = models.IntegerField(default=0)
    game_downloads = models.IntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Site visits: {self.site_visits}, Game downloads: {self.game_downloads}"

    def increment_site_visit(self):
        self.site_visits += 1
        self.save()

    def increment_game_download(self):
        self.game_downloads += 1
        self.save()

    class Meta:
        verbose_name = "Site Statistics"
        verbose_name_plural = "Site Statistics"
