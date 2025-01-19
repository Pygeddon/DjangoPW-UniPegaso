# Generated by Django 4.2.17 on 2025-01-14 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EventManager', '0015_alter_event_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventTags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
            },
        ),
        migrations.AddField(
            model_name='event',
            name='tags',
            field=models.ManyToManyField(related_name='events', to='EventManager.eventtags'),
        ),
    ]
