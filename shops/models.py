from django.db import models


class Contacts(models.Model):
    """Модель контактов"""
    title = models.CharField(max_length=75, verbose_name='Название фирмы')
    email = models.EmailField(unique=True, verbose_name='Почта фирмы')
    country = models.CharField(max_length=75, verbose_name='Страна фирмы')
    city = models.CharField(max_length=75, verbose_name='Город фирмы')
    street = models.CharField(max_length=75, verbose_name='Улица фирмы')
    house_number = models.CharField(max_length=75, verbose_name='Дом фирмы')

    class Meta:
        verbose_name = 'Контакты Фирмы'
        verbose_name_plural = 'Контакты фирмы'

    def __str__(self):
        return f'{self.title}'


class Product(models.Model):
    """Модель продукта"""
    title = models.CharField(max_length=75, verbose_name='Название')
    model = models.CharField(max_length=75, verbose_name='Модель')
    date_of_market_launch = models.DateField(verbose_name='дата выхода на рынок')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return f'{self.title}'


class Factory(models.Model):
    """Модель завода"""
    title = models.CharField(max_length=75, verbose_name='Название')
    contacts = models.ForeignKey(Contacts, on_delete=models.SET_NULL, verbose_name='Контакты',
                                 related_name='factory_contacts')
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, verbose_name='Продукты',
                                related_name='factory_Product')
    creation_time = models.DateTimeField(auto_now_add=True, verbose_name='Время и дата создания')

    class Meta:
        verbose_name = 'Завод'
        verbose_name_plural = 'Заводы'

    def __str__(self):
        return f'{self.title}'
