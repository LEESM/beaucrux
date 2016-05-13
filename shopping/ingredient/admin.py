from django.contrib import admin
from ingredient.models import Ingredient
from django_summernote.admin import SummernoteModelAdmin

class IngredientAdmin(SummernoteModelAdmin):
	list_display = ['kcia_no','ko_name','en_name','purpose','ewg_high_grade','ewg_low_grade','caution20','pub_date',]
admin.site.register(Ingredient, IngredientAdmin)

