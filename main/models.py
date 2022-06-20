from pyexpat import model
from statistics import mode
from django.db import models
import datetime
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth import get_user_model


class UserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Email is required')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_active', True)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        return self._create_user(email, password, **extra_fields)


class Student(AbstractUser):
    full_name = models.CharField(max_length=60)
    age = models.PositiveIntegerField(null=True)
    email = models.EmailField(max_length=150, unique=True)
    password = models.CharField(max_length=100, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

    def create_activation_code(self):
        import hashlib
        string_to_encode = self.email + str(self.id)
        encode_string = string_to_encode.encode()
        md5_object = hashlib.md5(encode_string)
        # хранится хешированный код каждого пользователя
        return md5_object

Student = get_user_model()

class Category(models.Model):
    name = models.CharField(verbose_name='Название категории', max_length=60)
    def __str__(self):
        return self.name


class Difficulty(models.Model):
    name = models.CharField(verbose_name='Сложность', max_length=40)
    def __str__(self):
        return self.name

class Task(models.Model):
    FIRST_LEVEL = 'FT_LV'
    SECOND_LEVEL = 'SC_LV'
    THIRD_LEVEL = 'TH_LV'
    LEVELS_CHOICES = [
        (FIRST_LEVEL, 'Уровень-1'),
        (SECOND_LEVEL, 'Уровень-2'),
        (THIRD_LEVEL, 'Уровень-3'),
    ]
    title = models.TextField(verbose_name='Текст задачи', max_length=255)
    difficulty = models.ForeignKey(Difficulty, on_delete=models.PROTECT, verbose_name='Сложность задачи')
    point = models.SmallIntegerField(verbose_name='Количество баллов')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Категория задачи')
    level = models.CharField(max_length=5, choices=LEVELS_CHOICES, default=FIRST_LEVEL)
    number_of_flag = models.SmallIntegerField(verbose_name='Количество флагов')
    hint = models.TextField(verbose_name='Подсказки')
    def __str__(self):
        return self.title


class Flag_Check(models.Model):
    task = models.ForeignKey(Task, verbose_name='Задача', on_delete=models.PROTECT)
    flag = models.CharField(verbose_name='Флаг', max_length=200)
    def __str__(self):
        return self.flag


class Group(models.Model):
    name = models.CharField(verbose_name='Группа', max_length=20)
    class Meta:
        managed = False

class St_Task(models.Model):
    student = models.ForeignKey(Student, verbose_name='Студент', on_delete=models.PROTECT)
    task = models.ForeignKey(Task, verbose_name='Задача', on_delete=models.PROTECT)
    point = models.SmallIntegerField()

