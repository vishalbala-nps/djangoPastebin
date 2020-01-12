from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class snips(models.Model):
    title = models.CharField(max_length=80, help_text='Enter a title')
    text = models.TextField(help_text='Enter the text')
    pubDate = models.DateTimeField() 

    def __str__(self):
        """String for representing the Model object."""
        return self.title+","+str(self.pubDate)


