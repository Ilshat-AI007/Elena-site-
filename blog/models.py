from django.db import models
from ckeditor.fields import RichTextField
import markdown

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextField()
    published_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True)

    def __str__(self):
        return self.title

    def content_as_html(self):
        return markdown.markdown(self.content)