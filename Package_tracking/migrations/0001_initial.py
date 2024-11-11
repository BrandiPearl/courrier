# Generated by Django 5.1.1 on 2024-11-11 16:52

import Package_tracking.models
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender_name', models.CharField(max_length=100)),
                ('sender_address', models.CharField(max_length=255)),
                ('sender_phone', models.CharField(max_length=20)),
                ('receiver_name', models.CharField(max_length=100)),
                ('receiver_email', models.EmailField(max_length=254)),
                ('receiver_phone', models.CharField(max_length=20)),
                ('receiver_address', models.CharField(max_length=255)),
                ('receiver_city', models.CharField(max_length=100)),
                ('receiver_state', models.CharField(max_length=100)),
                ('receiver_country', models.CharField(max_length=100)),
                ('tracking_id', models.CharField(default=Package_tracking.models.generate_tracking_id, editable=False, max_length=12, unique=True)),
                ('internal_uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('status', models.CharField(choices=[('processing', 'Processing'), ('shipped', 'Shipped'), ('in_transit', 'In Transit'), ('out_for_delivery', 'Out for Delivery'), ('delivered', 'Delivered'), ('canceled', 'Canceled'), ('returned', 'Returned')], default='processing', max_length=20)),
                ('delivery_method', models.CharField(choices=[('standard', 'Standard'), ('express', 'Express'), ('overnight', 'Overnight')], default='standard', max_length=20)),
                ('payment_method', models.CharField(choices=[('prepaid', 'Prepaid'), ('cod', 'Cash on Delivery'), ('third_party', 'Third Party Payment')], default='prepaid', max_length=20)),
                ('package_type', models.CharField(choices=[('document', 'Document'), ('box', 'Box'), ('pallet', 'Pallet'), ('other', 'Other')], default='box', max_length=20)),
                ('weight_kg', models.DecimalField(decimal_places=2, max_digits=10)),
                ('dimensions_cm', models.CharField(max_length=50)),
                ('insurance_value', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('fragile', models.BooleanField(default=False)),
                ('perishable', models.BooleanField(default=False)),
                ('signature_required', models.BooleanField(default=False)),
                ('pickup_date', models.DateTimeField(blank=True, null=True)),
                ('delivery_date', models.DateTimeField(blank=True, null=True)),
                ('estimated_delivery_date', models.DateTimeField(blank=True, null=True)),
                ('actual_delivery_date', models.DateTimeField(blank=True, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]