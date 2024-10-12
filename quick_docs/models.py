from django_extensions.db import models
from django_markdown_model.fields import MarkDownField
from django.db.models import Model


class Blog(models.TitleSlugDescriptionModel, models.TimeStampedModel):
    description = MarkDownField(null=True, blank=True)

    def __str__(self):
        return self.title
