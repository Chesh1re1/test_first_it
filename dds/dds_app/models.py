from django.db import models
from datetime import date


class Status(models.Model):
    name = models.CharField(
        max_length=256,
        unique=True,
        verbose_name = "Статус",
        blank=False,
        null=False
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'status'
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


class Type(models.Model):
    name = models.CharField(
        max_length=256,
        unique=True,
        verbose_name="Тип",
        blank=False,
        null=False
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'type'
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'


class Category(models.Model):
    type = models.ForeignKey(
        Type,
        on_delete=models.CASCADE,
        verbose_name="Тип",
        blank=False,
        null=False
    )
    name = models.CharField(
        max_length=256,
        unique=True,
        verbose_name="Категория",
        blank=False,
        null=False
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'category'
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Subcategory(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name="Категория",
        blank=False,
        null=False
    )
    name = models.CharField(
        max_length=256,
        unique=True,
        verbose_name="Подкатегория",
        blank=False,
        null=False
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'subcategory'
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'


class DDS(models.Model):
    date_create = models.DateField(
        default=date.today,
        verbose_name="Дата создания",
        blank=False,
        null=False
    )
    status = models.ForeignKey(
        Status,
        on_delete=models.CASCADE,
        verbose_name="Статус"
    )
    type = models.ForeignKey(
        Type,
        on_delete=models.CASCADE,
        verbose_name="Тип"
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name="Категория"
    )
    subcategory = models.ForeignKey(
        Subcategory,
        on_delete=models.CASCADE,
        verbose_name="Подкатегория"
    )
    sum = models.CharField(
        max_length=256,
        blank=False,
        null=False,
        verbose_name="Сумма"
    )
    comment = models.TextField(
        blank=True,
        null=True,
        verbose_name="Комментарий"
    )
    class Meta:
        db_table = 'dds'
        verbose_name = 'ДДС'
        verbose_name_plural = 'ДДС'