__all__ = []

# Standard library imports.

# Related third party imports.
from django.contrib import admin

# Local application/library specific imports.
from .models import Provider, Currency, CurrencyExchangeRate, Project, Users, Tasks, TaskStatus


class ProviderAdmin(admin.ModelAdmin):
    list_display = ('code', 'name')
    list_editable = ('name',)


class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('code', 'name')
    list_editable = ('name',)


class ReadOnlyAdminMixin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False


class CurrencyExchangeRateAdmin(admin.ModelAdmin):
    list_display = ('provider', 'from_currency', 'to_currency',
                    'rate', 'on_date')
    list_filter = ('provider', 'from_currency', 'to_currency')

    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
        else:
            return False


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'start_date', 'end_date', 'estimation_hours')
    list_editable = ('name',)


class UsersAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'surname', 'conctact', 'e_mail')
    list_editable = ('name',)


class TaskStatusAdmin(admin.ModelAdmin):
    list_display = ('code', 'name')
    list_editable = ('name',)


class TasksAdmin(admin.ModelAdmin):
    list_display = ('project', 'user', 'task_name', 'start_time', 'end_time', 'status', 'hours')
    list_filter = ('project', 'user')

    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
        else:
            return False


admin.site.register(Provider, ProviderAdmin)
admin.site.register(Currency, CurrencyAdmin)
admin.site.register(CurrencyExchangeRate, CurrencyExchangeRateAdmin)

admin.site.register(Project, ProjectAdmin)
admin.site.register(Users, UsersAdmin)
admin.site.register(TaskStatus, TaskStatusAdmin)
admin.site.register(Tasks, TasksAdmin)
