from django.db import models
from clients.models import Client

class Transfer(models.Model):
    sender = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="sender_transfers")
    receive = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="receive_transfers")
    balance = models.IntegerField(default=0, verbose_name="Баланс")
    
    def __str__(self):
        return f"{self.sender} - {self.receive}"
    
    def save(self, *args, **kwargs):
        sender = Client.objects.get(pk=self.sender.id)
        receive = Client.objects.get(pk=self.receive.id)
        if self.balance:
            if sender.balance >= self.balance:
                sender.balance -= self.balance
                receive.balance += self.balance
                sender.save()
                receive.save()
                super(Transfer, self).save(*args, **kwargs)
