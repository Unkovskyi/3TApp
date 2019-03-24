"""
doc string goes here
"""

__all__ = ['Provider', 'Currency', 'CurrencyExchangeRate', 'Project', 'Tasks', 'Users','TaskStatus']

# Standard library imports.

# Related third party imports.
from django.db import models
from django.utils.translation import ugettext_lazy as _
from datetime import datetime


# Local application/library specific imports.


class Provider(models.Model):
    code = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=200, blank=False)

    class Meta:
        db_table = 'provider'
        app_label = 'currency_exchange'
        verbose_name = _('Provider')
        verbose_name_plural = _('Providers')

    def __str__(self):
        return self.name or self.code


class Currency(models.Model):
    code = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=200, blank=False)

    class Meta:
        db_table = 'currency'
        app_label = 'currency_exchange'
        verbose_name = _('Currency')
        verbose_name_plural = _('Currencies')

    def __str__(self):
        return self.name or self.code


class CurrencyExchangeRate(models.Model):
    from_currency = models.ForeignKey(
        Currency,
        related_name='from_currency',
        on_delete=models.CASCADE
    )
    to_currency = models.ForeignKey(
        Currency,
        related_name='to_currency',
        on_delete=models.CASCADE
    )
    on_date = models.DateTimeField()
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    rate = models.DecimalField(max_digits=24, decimal_places=12)

    class Meta:
        db_table = 'currency_exchange_rate'
        app_label = 'currency_exchange'
        verbose_name = _('Currency Exchange Rate')
        verbose_name_plural = _('Currency Exchange Rates')





class Users(models.Model):
    code = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=200, blank=False)
    surname = models.CharField(max_length=200, blank=False)
    conctact = models.CharField(max_length=200, blank=False)
    e_mail = models.CharField(max_length=200, blank=False)

    class Meta:
        db_table = 'Users'
        app_label = 'currency_exchange'
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def __str__(self):
        return self.name or self.code


class Project(models.Model):
    code = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=200, blank=False)

    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    estimation_hours = models.DecimalField(max_digits=15, decimal_places=2)

    class Meta:
        db_table = 'projects'
        app_label = 'currency_exchange'
        verbose_name = _('Project')
        verbose_name_plural = _('Projects')

    def __str__(self):
        return self.name or self.code



class TaskStatus(models.Model):
    code = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=200, blank=False)

    class Meta:
        db_table = 'task_status'
        app_label = 'currency_exchange'
        verbose_name = _('Task Status')
        verbose_name_plural = _('Task Status')

    def __str__(self):
        return self.name or self.code




class Tasks(models.Model):

    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    task_name = models.CharField(default='',max_length=200, blank=False)
    task_description = models.CharField(default='',max_length=200, blank=False)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    hours = models.DecimalField(max_digits=15, decimal_places=2)
    status = models.ForeignKey(TaskStatus, on_delete=models.CASCADE)

    class Meta:
        db_table = 'tasks'
        app_label = 'currency_exchange'
        verbose_name = _('Task')
        verbose_name_plural = _('Tasks')

