from django.db import models
from django.utils.translation import gettext_lazy as _

# # Create your models here.


class Note(models.Model):
    """Model definition for Note."""

    title = models.CharField(_("title"), max_length=50)
    content = models.TextField(_("content"))

    # TODO: Define fields here

    class Meta:
        """Meta definition for Note."""

        verbose_name = "Note"
        verbose_name_plural = "Notes"

    def __str__(self):
        """Unicode representation of Note."""
        return str(self.title)
