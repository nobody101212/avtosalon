from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='Марка')),
                ('slug', models.SlugField(unique=True)),
            ],
            options={'verbose_name': 'Марка', 'verbose_name_plural': 'Марки'},
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('model', models.CharField(max_length=100, verbose_name='Модель')),
                ('year', models.PositiveIntegerField(verbose_name='Год выпуска')),
                ('price', models.DecimalField(decimal_places=0, max_digits=12, verbose_name='Цена (₸)')),
                ('mileage', models.PositiveIntegerField(default=0, verbose_name='Пробег (км)')),
                ('engine_volume', models.DecimalField(decimal_places=1, max_digits=3, verbose_name='Объём (л)')),
                ('horsepower', models.PositiveIntegerField(verbose_name='Мощность (л.с.)')),
                ('fuel', models.CharField(choices=[('petrol','Бензин'),('diesel','Дизель'),('hybrid','Гибрид'),('electric','Электро')], default='petrol', max_length=20, verbose_name='Топливо')),
                ('transmission', models.CharField(choices=[('auto','Автомат'),('manual','Механика'),('robot','Робот')], default='auto', max_length=20, verbose_name='КПП')),
                ('condition', models.CharField(choices=[('new','Новый'),('used','С пробегом')], default='new', max_length=10, verbose_name='Состояние')),
                ('body', models.CharField(choices=[('sedan','Седан'),('suv','Кроссовер'),('hatchback','Хэтчбек'),('minivan','Минивэн'),('coupe','Купе')], default='sedan', max_length=20, verbose_name='Кузов')),
                ('color', models.CharField(blank=True, max_length=50, verbose_name='Цвет')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('image', models.ImageField(blank=True, null=True, upload_to='cars/', verbose_name='Фото')),
                ('is_featured', models.BooleanField(default=False, verbose_name='Хит продаж')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.brand', verbose_name='Марка')),
            ],
            options={'verbose_name': 'Автомобиль', 'verbose_name_plural': 'Автомобили', 'ordering': ['-created_at']},
        ),
        migrations.CreateModel(
            name='LeadRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('phone', models.CharField(max_length=20, verbose_name='Телефон')),
                ('request_type', models.CharField(choices=[('testdrive','Тест-драйв'),('credit','Кредит'),('tradein','Trade-in'),('consult','Консультация')], default='consult', max_length=20, verbose_name='Тип')),
                ('message', models.TextField(blank=True, verbose_name='Сообщение')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_processed', models.BooleanField(default=False, verbose_name='Обработана')),
                ('car', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cars.car', verbose_name='Автомобиль')),
            ],
            options={'verbose_name': 'Заявка', 'verbose_name_plural': 'Заявки', 'ordering': ['-created_at']},
        ),
    ]