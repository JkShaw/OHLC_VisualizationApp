from django.db import models


class StockData(models.Model):
    """Stock records containg OHLC for a stock."""

    date = models.DateField(max_length=20)
    open = models.FloatField(default=0.0)
    high = models.FloatField(default=0.0)
    low = models.FloatField(default=0.0)
    close = models.FloatField(default=0.0)
    volume = models.IntegerField(default=0)
    adjusted = models.FloatField(default=0)
    stock = models.IntegerField(default=0)

    def __str__(self):
        """Return trade date."""
        return str(self.date)
