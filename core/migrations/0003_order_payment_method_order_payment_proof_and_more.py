# Generated by Django 4.2.11 on 2025-06-15 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_customer_customer_code_customer_qr_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='payment_method',
            field=models.CharField(choices=[('CASH', 'Efectivo'), ('YAPE', 'Yape'), ('PLIN', 'Plin')], default='CASH', max_length=20),
        ),
        migrations.AddField(
            model_name='order',
            name='payment_proof',
            field=models.ImageField(blank=True, null=True, upload_to='payment_proofs/'),
        ),
        migrations.AddField(
            model_name='order',
            name='payment_status',
            field=models.CharField(choices=[('PENDING', 'Falta Pagar'), ('PAID', 'Pagado'), ('PARTIAL', 'Parcialmente Pagado')], default='PENDING', max_length=20),
        ),
    ]
