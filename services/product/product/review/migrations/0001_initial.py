# Generated by Django 3.0.10 on 2022-05-19 19:21

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('is_active', models.BooleanField(blank=True, default=True, null=True, verbose_name='is_active')),
                ('is_deleted', models.BooleanField(blank=True, default=False, null=True, verbose_name='is_deleted')),
                ('author', models.BigIntegerField(blank=True, null=True, verbose_name='Author')),
                ('rating', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Rating')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Comment')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_reviews', to='product.Product')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
