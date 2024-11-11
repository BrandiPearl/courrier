import uuid
import random
import string
from django.db import models

def generate_tracking_id():
    """Generate a tracking ID with the prefix 'SEDX' and a random 6-digit alphanumeric code."""
    prefix = "SEDX"
    suffix = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    return f"{prefix}{suffix}"

class Package(models.Model):
    STATUS_CHOICES = [
        ('processing', 'Processing'),
        ('shipped', 'Shipped'),
        ('in_transit', 'In Transit'),
        ('out_for_delivery', 'Out for Delivery'),
        ('delivered', 'Delivered'),
        ('canceled', 'Canceled'),
        ('returned', 'Returned'),
    ]

    PAYMENT_CHOICES = [
        ('prepaid', 'Prepaid'),
        ('cod', 'Cash on Delivery'),
        ('third_party', 'Third Party Payment'),
    ]

    DELIVERY_METHODS = [
        ('standard', 'Standard'),
        ('express', 'Express'),
        ('overnight', 'Overnight'),
    ]

    PACKAGE_TYPES = [
        ('document', 'Document'),
        ('box', 'Box'),
        ('pallet', 'Pallet'),
        ('other', 'Other'),
    ]

    TRANSPORTATION_MODES = [
        ('truck', 'Truck'),
        ('air', 'Air'),
        ('ship', 'Ship'),
        ('train', 'Train'),
        ('other', 'Other'),
    ]

    sender_name = models.CharField(max_length=100)
    sender_address = models.CharField(max_length=255)
    sender_phone = models.CharField(max_length=20)

    receiver_name = models.CharField(max_length=100)
    receiver_email = models.EmailField()
    receiver_phone = models.CharField(max_length=20)
    receiver_address = models.CharField(max_length=255)
    receiver_city = models.CharField(max_length=100)
    receiver_state = models.CharField(max_length=100)
    receiver_country = models.CharField(max_length=100)

    tracking_id = models.CharField(max_length=12, unique=True, default=generate_tracking_id, editable=False)
    internal_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)  # For internal use

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='processing')
    delivery_method = models.CharField(max_length=20, choices=DELIVERY_METHODS, default='standard')
    payment_method = models.CharField(max_length=20, choices=PAYMENT_CHOICES, default='prepaid')
    package_type = models.CharField(max_length=20, choices=PACKAGE_TYPES, default='box')

    weight_kg = models.DecimalField(max_digits=10, decimal_places=2)
    dimensions_cm = models.CharField(max_length=50)  # e.g., "50x40x30"

    insurance_value = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    fragile = models.BooleanField(default=False)
    perishable = models.BooleanField(default=False)
    signature_required = models.BooleanField(default=False)

    pickup_date = models.DateTimeField(null=True, blank=True)
    delivery_date = models.DateTimeField(null=True, blank=True)

    estimated_delivery_date = models.DateTimeField(null=True, blank=True)
    actual_delivery_date = models.DateTimeField(null=True, blank=True)

    notes = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # New fields
    current_location = models.CharField(max_length=255, null=True, blank=True)
    transportation_mode = models.CharField(max_length=20, choices=TRANSPORTATION_MODES, default='truck')

    def __str__(self):
        return f"{self.tracking_id} - {self.receiver_name}"