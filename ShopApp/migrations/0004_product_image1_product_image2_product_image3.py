# Generated by Django 4.0.4 on 2022-04-17 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShopApp', '0003_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Image1',
            field=models.ImageField(blank='True', null='True', upload_to='productpics'),
            preserve_default='True',
        ),
        migrations.AddField(
            model_name='product',
            name='Image2',
            field=models.ImageField(blank='True', null='True', upload_to='productpics'),
            preserve_default='True',
        ),
        migrations.AddField(
            model_name='product',
            name='Image3',
            field=models.ImageField(blank='True', null='True', upload_to='productpics'),
            preserve_default='True',
        ),
    ]