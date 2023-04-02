from django.contrib import admin
from .models import Counselor, CounselorTag, CounselorCert


@admin.register(Counselor)
class CounselorAdmin(admin.ModelAdmin):
    pass




@admin.register(CounselorTag)
class CounselorTagAdmin(admin.ModelAdmin):
    pass


@admin.register(CounselorCert)
class CounselorCertAdmin(admin.ModelAdmin):
    pass

# @admin.register(CounselorExp)
# class CounselorExpAdmin(admin.ModelAdmin):
#     pass

# @admin.register(CounselorTime)
# class CounselorTimeAdmin(admin.ModelAdmin):
#     pass
