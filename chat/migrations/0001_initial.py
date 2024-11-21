# Generated by Django 5.1.2 on 2024-11-21 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.CharField(max_length=100)),
                ('message', models.TextField(blank=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='uploads/')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]