# Generated by Django 4.2.17 on 2025-01-03 11:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('EventManager', '0005_alter_event_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Thumbnail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EventManager.event')),
            ],
        ),
    ]
