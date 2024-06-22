from django.db import models


class Contact(models.Model):
    class Meta:
        verbose_name_plural = "Contact Messages"
        
    contact_name = models.CharField(max_length=200, null=False, blank=False)
    contact_email = models.EmailField(max_length=200, null=False, blank=False)
    contact_message = models.TextField(max_length=1000, null=False, blank=False)
    contact_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.contact_name