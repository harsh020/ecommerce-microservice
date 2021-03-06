# Generated by Django 3.0.10 on 2022-05-22 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(blank=True, max_length=100, null=True, verbose_name='Country')),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(blank=True, max_length=100, null=True, verbose_name='State')),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='country_state', to='core.Country')),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(blank=True, max_length=100, null=True, verbose_name='City')),
                ('state', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='state_city', to='core.State')),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(blank=True, max_length=10, null=True, verbose_name='Phone Number')),
                ('full_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Full Name')),
                ('house_number', models.CharField(blank=True, max_length=20, null=True, verbose_name='House Number')),
                ('area', models.CharField(blank=True, max_length=50, null=True, verbose_name='Area')),
                ('landmark', models.CharField(blank=True, max_length=50, null=True, verbose_name='Landmark')),
                ('pincode', models.CharField(blank=True, max_length=6, null=True, verbose_name='Pincode')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='city_address', to='core.City')),
                ('country', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='country_address', to='core.Country')),
                ('state', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='state_address', to='core.State')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
