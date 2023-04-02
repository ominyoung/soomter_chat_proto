from django.db import models


class Counselor(models.Model):
    """
        상담사 DB
    """
    name = models.CharField("Name", max_length=80)
    sentence = models.CharField("Sentence", max_length=250, null=True, blank=True)
    profile_image = models.ImageField("Img", upload_to='counselor/%Y/%m/%d', null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Counselor DB'
        db_table = 'counselors'

    def __str__(self):
        return self.name


class Abstract_counselor(models.Model):
    content = models.TextField("Content")
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.content


class CounselorCert(Abstract_counselor):
    """
        상담사 자격증 DB
    """
    counselor = models.ForeignKey(Counselor, on_delete=models.CASCADE, related_name='counselor_cert')

    class Meta:
        verbose_name_plural = 'Counselor_Cert DB'
        db_table = 'counselor_certs'


class CounselorTag(Abstract_counselor):
    """
        상담사 태그 DB
    """
    counselor = models.ForeignKey(Counselor, on_delete=models.CASCADE, related_name='counselor_tag')

    class Meta:
        verbose_name_plural = 'Counselor_Tag DB'
        db_table = 'counselor_tags'


# class CounselorExp(Abstract_counselor):
#     counselor = models.ForeignKey(Counselor, on_delete=models.CASCADE, related_name='counselor_exp')
#
#     class Meta:
#         verbose_name_plural = "Counselor_Exp DB"
#         db_table = 'counselor_exps'


# class CounselorTime(Abstract_counselor):
#     counselor = models.ForeignKey(Counselor, on_delete=models.CASCADE, related_name='counselor_time')
#
#     class Meta:
#         verbose_name_plural = "Counselor_Time DB"
#         db_table = 'counselor_times'
