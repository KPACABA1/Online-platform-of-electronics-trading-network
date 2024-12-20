from django.contrib import admin

from shops.models import Contacts, Product, Factory, RetailNetwork, IndividualEntrepreneur


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    """Админка для контактов."""
    list_display = ('id', 'title', 'email')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Админка для продуктов."""
    list_display = ('id', 'title')


@admin.register(Factory)
class FactoryAdmin(admin.ModelAdmin):
    """Админка для завода."""
    list_display = ('id', 'title')


@admin.register(RetailNetwork)
class RetailNetworkAdmin(admin.ModelAdmin):
    """Админка для розничной сети."""
    list_display = ('id', 'title')


@admin.register(IndividualEntrepreneur)
class IndividualEntrepreneurAdmin(admin.ModelAdmin):
    """Админка для индивидуального предпринимателя."""
    list_display = ('id', 'title')
