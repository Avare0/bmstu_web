# Generated by Django 3.2.7 on 2021-10-30 18:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house_photos',
            name='house',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='house_photo', to='api_app.houses'),
        ),
    ]
