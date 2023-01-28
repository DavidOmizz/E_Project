# Generated by Django 4.0.6 on 2023-01-28 19:04

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=255)),
                ('customer_email', models.EmailField(max_length=254)),
                ('Shipping_address', models.TextField()),
                ('customer_number', models.TextField()),
                ('message', models.TextField()),
                ('quantity', models.IntegerField()),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.IntegerField(choices=[(0, 'pending'), (1, 'processing'), (2, 'shipped'), (3, 'delivered')], default=0)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='my_app.product')),
            ],
            options={
                'ordering': ('-created_on',),
            },
        ),
    ]
