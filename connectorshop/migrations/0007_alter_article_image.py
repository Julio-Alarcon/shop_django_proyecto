# Generated by Django 4.1.6 on 2023-02-12 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connectorshop', '0006_alter_article_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(default='images/nullproduct.jpg', upload_to='images/'),
        ),
    ]
