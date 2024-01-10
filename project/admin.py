from django.contrib import admin
from project.models import Project, PaymentChannel, Refback, Insurance


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'started_at', 'created_at')
    list_display_links = ('id', 'name')


class PaymentChannelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_active')
    list_editable = ('is_active',)


class RefbackAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'login','wallet','payment_channel','project')
    list_display_links = ('id', 'email', 'login')


class InsuranceAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'login', 'wallet', 'payment_channel', 'project')
    list_display_links = ('id', 'email', 'login')


# Register your models here.
admin.site.register(Project, ProjectAdmin)
admin.site.register(PaymentChannel, PaymentChannelAdmin)
admin.site.register(Refback, RefbackAdmin)
admin.site.register(Insurance, InsuranceAdmin)


