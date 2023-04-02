from django.db import models


class Banner(models.Model):
    """
        배너 DB
    """
    name = models.CharField("Name", max_length=80)
    start_date = models.DateField("Start_Date")
    end_date = models.DateField("End_Date")
    img = models.ImageField("Img", upload_to='banners/%Y/%m/%d', null=True, blank=True)
    link_to = models.TextField("Link")

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Banner DB'
        db_table = 'banners'

    def __str__(self):
        return self.name

