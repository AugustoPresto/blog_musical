from django.db import models
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

POST_TYPES = [
    ("Notícia", "Notícia"),
    ("Resenha", "Resenha")
]

User = get_user_model()


class Post(models.Model):
    title = models.CharField(max_length=255)
    summary = RichTextField()
    content = RichTextUploadingField()
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    post_type = models.CharField(max_length=20,
                                 default='Notícia',
                                 choices=POST_TYPES)
    post_img = models.ImageField(upload_to='images/')
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
