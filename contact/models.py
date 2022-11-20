from django.db import models
from django.urls import reverse
from PIL import Image

class Contact(models.Model):
    RELATIONSHIP =  (
        ('family','Family'),
        ('friend','Friend'),
        ('work','Work'),
        ('other','Other'),
    )
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    relationship = models.CharField(choices=RELATIONSHIP,max_length=200)
    profile = models.ImageField(
        upload_to='profile_pics',
        blank=True,
        null=True,
        default='default.png'
    )
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('contact-profile', kwargs={'pk': self.pk})

    # set image size 
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.profile.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.profile.path)

