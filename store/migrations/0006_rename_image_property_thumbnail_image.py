# Generated by Django 4.1.3 on 2023-01-03 07:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_property_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='property',
            old_name='image',
            new_name='thumbnail',
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='uploads/product_images')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.property')),
            ],
        ),
    ]
