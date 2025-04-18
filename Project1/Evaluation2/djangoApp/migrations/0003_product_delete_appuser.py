# Generated by Django 5.2 on 2025-04-14 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoApp', '0002_appuser_delete_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='product_images/')),
                ('category', models.CharField(choices=[('all', 'All'), ('pharmacy', 'Pharmacy'), ('grocery', 'Grocery'), ('beauty', 'Beauty'), ('snacks', 'Snacks')], max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='AppUser',
        ),
    ]
