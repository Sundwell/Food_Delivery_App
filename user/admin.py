from django.contrib import admin
from user.models import User, Activity


class ActivityAdmin(admin.ModelAdmin):
    fields = ('activity',)


admin.site.register(User)
admin.site.register(Activity, ActivityAdmin)
