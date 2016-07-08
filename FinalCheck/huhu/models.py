from __future__ import unicode_literals

from django.db import models

# Create your models here.

class PlayerPosition(models.Model):
	player1Position = models.IntegerField()
	player2Position = models.IntegerField()

class Dice(models.Model):
	dice1 = models.IntegerField()
	dice2 = models.IntegerField()

class Seperate(models.Model):
	seperMine = models.IntegerField()
	count = models.IntegerField()

class Order(models.Model):
	order = models.IntegerField()

class PickMine(models.Model):
	pick = models.IntegerField()

class SeperMine(models.Model):
	mine = models.IntegerField()