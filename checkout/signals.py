from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from .models import OrderLineItem


@reciever(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    instance.order.update_total()

@reciever(post_delete, sender=OrderLineItem)
def update_delete(sender, instance, **kwargs):
    instance.order.update_total()


