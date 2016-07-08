from django.contrib import admin


from .models import PlayerPosition
from .models import Dice
from .models import Seperate
from .models import Order
from .models import PickMine
from .models import SeperMine
# Register your models here.

admin.site.register(PlayerPosition)
admin.site.register(Dice)
admin.site.register(Seperate)
admin.site.register(Order)
admin.site.register(PickMine)
admin.site.register(SeperMine)