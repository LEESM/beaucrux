from django.contrib import admin
from ingredient.models import ingredient
from django_summernote.admin import SummernoteModelAdmin

class ingredientAdmin(SummernoteModelAdmin):
	list_display = ['kcia_no','ko_name','en_name','purpose','ewg_high_grade','ewg_low_grade','caution20','pub_date',]

admin.site.register(ingredient, ingredientAdmin)

