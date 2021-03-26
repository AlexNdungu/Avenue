# Generated by Django 3.1.1 on 2021-02-11 09:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('avenueShop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buy_type', models.CharField(max_length=100, null=True)),
                ('cost', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Incomplete', 'Incomplete'), ('Complete', 'Complete')], max_length=100, null=True)),
                ('time_pick', models.TimeField(null=True)),
                ('date_pick', models.DateField(null=True)),
                ('buys_types', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='usersAvenue.buy')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='avenueShop.movies')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('phone', models.CharField(max_length=100, null=True)),
                ('my_pic', models.ImageField(blank=True, default='my-def.jpg', null=True, upload_to='images/')),
                ('email', models.CharField(max_length=200, null=True)),
                ('recidence', models.CharField(max_length=100, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('genre', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='avenueShop.genre')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
