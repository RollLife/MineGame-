from django.shortcuts import render
from .models import Seperate
from .models import Dice
from .models import PlayerPosition
from .models import Order
from .models import PickMine
from .models import SeperMine
import random

# Create your views here.

def index(request):
	seperate = Seperate.objects.all()
	dice = Dice.objects.all().last()
	playerP = PlayerPosition.objects.all().last()
	orders = Order.objects.all().last()
	picks = PickMine.objects.all().last()
	mines = SeperMine.objects.all().last()
	return render(request,'main/index.html', {'seperate':seperate,'dice':dice,'playerP':playerP,'orders':orders,'picks':picks,'mines':mines})

def insert(request):
	road = []
	for i in range(0,112):
		road.append(0)
	mineCount = 0
	count = 1

	while mineCount != 10:
		mine = random.randrange(0, 100)
		if road[mine]==0:
			road[mine] = 1
			mineCount = mineCount + 1

	for a in range(0, 112):
		seperate = Seperate()
		if a == 99:
			seperate.seperMine = 2
			seperate.count = count
			count = count + 1
			seperate.save()
		elif road[a]==0:
			seperate.seperMine = 0
			seperate.count = count
			count = count + 1
			seperate.save()
		elif road[a]==1:
			seperate.seperMine = 1
			seperate.count = count
			count = count + 1
			seperate.save()

	playerp = PlayerPosition()
	playerp.player1Position = 0
	playerp.player2Position = 0
	playerp.save()
	orders = Order()
	orders.order = 1
	orders.save()
	return render(request, 'main/insert.html', {})

def passnext(request):
	dice = Dice()
	dices1 = random.randrange(1, 7)
	dices2 = random.randrange(1, 7)
	dice.dice1 = dices1
	dice.dice2 = dices2
	dice.save()

#	playerp = PlayerPosition()
#	playerp.player1Position = dice.dice1+dice.dice2
#	playerp.player2Position = 0
#	playerp.save()
	orders = Order.objects.all().last()
	orderc = Order()
	pickmine = PickMine()
	sepermine = SeperMine()
	sepermine.mine = 0
	if orders.order == 1:
		position = PlayerPosition.objects.all().last()
		position.player1Position = position.player1Position + dice.dice1 + dice.dice2
		#mine check if while mun
		seperate = Seperate.objects.get(count=position.player1Position)
		if seperate.seperMine == 1:
			pickmine.pick = position.player1Position
			position.player1Position = position.player1Position - 2
			sepermine.mine = 1
			pickmine.save()
			sepermine.save()
		"""if  :
			position.player1Position = position.player1Position - 2
			print "mine" <- mine  ////   database Seperate insert colomn count """
		orderc.order = 0
		if dice.dice1 == dice.dice2 :
			orderc.order =1
		if position.player1Position >=100:
			orderc.order =2
		if position.player1Position <0:
			position.player1Position = 0
		position.save()
		orderc.save()
	

	elif orders.order ==0:
		sepermine.mine = 0
		position = PlayerPosition.objects.all().last()
		position.player2Position = position.player2Position + dice.dice1 + dice.dice2
		seperate = Seperate.objects.get(count=position.player2Position)
		if seperate.seperMine == 1:
			pickmine.pick = position.player1Position
			position.player2Position = position.player2Position - 2
			sepermine.mine = 1
			pickmine.save()
			sepermine.save()
		"""if position.player1Position :
			position.player1Position = position.player1Position - 2
			print "mine"  <- mine  ////   database Seperate insert colomn count """
		orderc.order = 1
		if dice.dice1 == dice.dice2 :
			orderc.order =0
		if position.player2Position >=100:
			orderc.order =2
		if position.player2Position <0:
			position.player2Position = 0
		position.save()
		orderc.save()
	sepermine.save()	
	return render(request, 'main/passnext.html', {})

def deleteaction(request):
	seperate = Seperate.objects.all()
	seperate.delete()
	dice = Dice.objects.all()
	dice.delete()
	position = PlayerPosition.objects.all()
	position.delete()
	order = Order.objects.all()
	order.delete()
	pick = PickMine.objects.all()
	pick.delete()
	mine = SeperMine.objects.all()
	mine.delete()
	return render(request, 'main/deleteaction.html', {})
