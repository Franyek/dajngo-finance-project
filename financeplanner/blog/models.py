from django.db import models


class BlogPost(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField("date published")
    title = models.CharField(max_length=100)

    def get_first_paragraph(self):
        return self.text.splitlines()[0]

    def __str__(self):
        return self.title
