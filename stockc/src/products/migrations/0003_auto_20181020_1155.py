# Generated by Django 2.1.2 on 2018-10-20 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20181020_1141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='colour',
            field=models.CharField(choices=[('B', 'Black'), ('W', 'White'), ('L', 'Blue'), ('E', 'Grey'), ('G', 'Green')], max_length=1),
        ),
        migrations.AlterField(
            model_name='product',
            name='list_price',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='max_qty',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='product',
            name='min_qty',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='product',
            name='qty',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='product',
            name='standard_price',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='weight',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=6, null=True),
        ),
    ]