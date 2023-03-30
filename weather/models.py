from django.db import models


class City(models.Model):
    code = models.CharField(max_length=10, verbose_name="Kody", primary_key=True)
    name = models.CharField(max_length=50, verbose_name="Ady")

    class Meta:
        verbose_name_plural = "Şäherler we Şäherçeler"

    def __str__(self):
        return self.name


class DailyForecast(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name="Ýeri", related_name="city")
    date = models.DateField(auto_now_add=False, verbose_name="Senesi")
    temp_min = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="minimum temperatura")
    temp_max = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="maximum temperatura")
    unit = models.CharField(max_length=10, verbose_name="Temperaturanyň ölçeg birligi")


    class Meta:
        # ordering = ("-date",)
        verbose_name_plural = "Gündelik Howa Maglumaty"
    
    def __str__(self):
        return str(self.city.name)


class Day(models.Model):
    day = models.ForeignKey(DailyForecast, on_delete=models.CASCADE, related_name="day", verbose_name="Senesi")
    iconPhrase = models.CharField(max_length=100, verbose_name="Gysgaça")
    rain = models.IntegerField(verbose_name="ýagyş ähtimallygy")
    snow = models.IntegerField(verbose_name="gar ähtimallygy")
    ice = models.IntegerField(verbose_name="doňaklyk ähtimallygy")
    wind_speed = models.DecimalField(decimal_places=2, max_digits=6, verbose_name="Şemalyň tizligi")
    wind_direction = models.CharField(max_length=10, verbose_name="Şemalyň ugry")
    wind_unit = models.CharField(max_length=5, verbose_name="Şemal tizliginiň ölçeg birligi", blank=True, null=True)


    class Meta:
        verbose_name_plural = "Gündizine"

    def __str__(self):
        return str(self.day.date)


class Night(models.Model):
    day = models.ForeignKey(DailyForecast, on_delete=models.CASCADE, related_name="night", verbose_name="Senesi")
    iconPhrase = models.CharField(max_length=100, verbose_name="Gysgaça")
    rain = models.IntegerField(verbose_name="ýagyş ähtimallygy")
    snow = models.IntegerField(verbose_name="gar ähtimallygy")
    ice = models.IntegerField(verbose_name="doňaklyk ähtimallygy")
    wind_speed = models.DecimalField(decimal_places=2, max_digits=6, verbose_name="Şemalyň tizligi")
    wind_direction = models.CharField(max_length=10, verbose_name="Şemalyň ugry")
    wind_unit = models.CharField(max_length=5, verbose_name="Şemal tizliginiň ölçeg birligi", blank=True, null=True)

    class Meta:
        verbose_name_plural = "Gijesine"

    def __str__(self):
        return str(self.day.date)
