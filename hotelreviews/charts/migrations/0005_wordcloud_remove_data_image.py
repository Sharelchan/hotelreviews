# Generated by Django 5.0.2 on 2024-02-25 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charts', '0004_data_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='wordcloud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
        migrations.RemoveField(
            model_name='data',
            name='image',
        ),
    ]