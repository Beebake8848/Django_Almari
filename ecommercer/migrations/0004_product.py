# Generated by Django 4.1.5 on 2023-05-18 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommercer', '0003_remove_userinfo_name_userinfo_password_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]