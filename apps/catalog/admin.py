from django.contrib import admin

from apps.catalog.models import Logo, Car, Contract


@admin.register(Logo)
class LogoAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('title', )


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ('month', 'year')
