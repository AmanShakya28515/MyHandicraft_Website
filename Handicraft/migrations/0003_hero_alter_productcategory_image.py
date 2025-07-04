# Generated by Django 5.0.1 on 2024-11-09 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Handicraft', '0002_productcategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='static/')),
            ],
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='image',
            field=models.ImageField(upload_to='categories/'),
        ),
    ]
