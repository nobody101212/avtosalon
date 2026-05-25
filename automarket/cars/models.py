from django.db import models


class Brand(models.Model):
    name = models.CharField('Марка', max_length=100)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Марка'
        verbose_name_plural = 'Марки'

    def __str__(self):
        return self.name


class Car(models.Model):
    FUEL_CHOICES = [
        ('petrol', 'Бензин'), ('diesel', 'Дизель'),
        ('hybrid', 'Гибрид'), ('electric', 'Электро'),
    ]
    TRANSMISSION_CHOICES = [
        ('auto', 'Автомат'), ('manual', 'Механика'), ('robot', 'Робот'),
    ]
    CONDITION_CHOICES = [
        ('new', 'Новый'), ('used', 'С пробегом'),
    ]
    BODY_CHOICES = [
        ('sedan', 'Седан'), ('suv', 'Кроссовер'),
        ('hatchback', 'Хэтчбек'), ('minivan', 'Минивэн'), ('coupe', 'Купе'),
    ]

    brand        = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name='Марка')
    model        = models.CharField('Модель', max_length=100)
    year         = models.PositiveIntegerField('Год выпуска')
    price        = models.DecimalField('Цена (₸)', max_digits=12, decimal_places=0)
    mileage      = models.PositiveIntegerField('Пробег (км)', default=0)
    engine_volume= models.DecimalField('Объём (л)', max_digits=3, decimal_places=1)
    horsepower   = models.PositiveIntegerField('Мощность (л.с.)')
    fuel         = models.CharField('Топливо', max_length=20, choices=FUEL_CHOICES, default='petrol')
    transmission = models.CharField('КПП', max_length=20, choices=TRANSMISSION_CHOICES, default='auto')
    condition    = models.CharField('Состояние', max_length=10, choices=CONDITION_CHOICES, default='new')
    body         = models.CharField('Кузов', max_length=20, choices=BODY_CHOICES, default='sedan')
    color        = models.CharField('Цвет', max_length=50, blank=True)
    description  = models.TextField('Описание', blank=True)
    image        = models.ImageField('Фото', upload_to='cars/', blank=True, null=True)
    is_featured  = models.BooleanField('Хит продаж', default=False)
    created_at   = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.brand.name} {self.model} {self.year}'


class LeadRequest(models.Model):
    REQUEST_TYPES = [
        ('testdrive', 'Тест-драйв'), ('credit', 'Кредит'),
        ('tradein', 'Trade-in'), ('consult', 'Консультация'),
    ]

    name         = models.CharField('Имя', max_length=100)
    phone        = models.CharField('Телефон', max_length=20)
    car          = models.ForeignKey(Car, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Автомобиль')
    request_type = models.CharField('Тип', max_length=20, choices=REQUEST_TYPES, default='consult')
    message      = models.TextField('Сообщение', blank=True)
    created_at   = models.DateTimeField(auto_now_add=True)
    is_processed = models.BooleanField('Обработана', default=False)

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.name} — {self.phone}'