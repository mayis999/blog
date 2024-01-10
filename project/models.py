from django.db import models

# Create your models here.


class Project(models.Model):
    class WithdrawType(models.TextChoices):
        INSTANT = 'INS', 'Instant'
        MANUAl = 'MAN', 'Manual'

    class ProfitType(models.TextChoices):
        # Please do not concentrate on namings
        HIGH = 'H', 'Highly profitable'
        MIDDLE = 'M', 'Middle profitable'
        LOW = 'L', 'Low profitable'

    name = models.CharField(max_length=64)
    description = models.TextField()

    min_deposit = models.CharField(max_length=16)
    min_withdraw = models.CharField(max_length=16)

    profit_description = models.CharField(max_length=64)
    affiliate_program = models.CharField(max_length=16)

    insurance_amount = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    currency = models.CharField(max_length=8)
    our_deposit = models.DecimalField(max_digits=7, decimal_places=2)
    our_withdraw = models.DecimalField(max_digits=7, decimal_places=2)

    youtube_link = models.URLField()
    link = models.URLField()

    withdraw_type = models.CharField(max_length=4, choices=WithdrawType.choices)
    profit_type = models.CharField(max_length=2, choices=ProfitType.choices)
    is_scam = models.BooleanField(default=True)

    started_at = models.DateField()
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    def __str__(self):
        return self.name


class PaymentChannel(models.Model):
    name = models.CharField(max_length=16)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Payment Channel'
        verbose_name_plural = 'Payment Channels'

    def __str__(self):
        return self.name


class Refback(models.Model):
    email = models.EmailField()
    login = models.CharField(max_length=256)
    deposited_at = models.DateField()
    deposit = models.DecimalField(max_digits=7, decimal_places=2)
    wallet = models.CharField(max_length=256)
    payment_channel = models.ForeignKey(PaymentChannel, on_delete=models.PROTECT)
    project = models.ForeignKey(Project, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Refback'
        verbose_name_plural = 'Refbacks'



class Insurance(models.Model):
    email = models.EmailField()
    login = models.CharField(max_length=256)
    withdraw = models.DecimalField(max_digits=7, decimal_places=2)
    wallet = models.CharField(max_length=256)

    payment_channel = models.ForeignKey(PaymentChannel, on_delete=models.PROTECT)
    project = models.ForeignKey(Project, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Insurance'
        verbose_name_plural = 'Insurances'

