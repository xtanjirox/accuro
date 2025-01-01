from django.db import models


class TransactionStatus(models.TextChoices):
    PAID = "Paid", "Paid"
    DUE = "Due", "Due"
    CANCELLED = "Cancelled", "Cancelled"


class TransactionType(models.TextChoices):
    INCOME = "Income", "Income"
    EXPENSE = "Expense", "Expense"


class Transaction(models.Model):
    customer = models.CharField(max_length=150)
    transaction_date = models.DateField()
    due_date = models.DateField()
    total = models.DecimalField(max_digits=20, decimal_places=2)
    status = models.CharField(
        max_length=20, choices=TransactionStatus.choices, default=TransactionStatus.DUE)
    transaction_type = models.CharField(
        max_length=20, choices=TransactionType.choices, default=TransactionType.EXPENSE)

    def __str__(self):
        return self.customer
