from django.contrib import admin
from .models import Brand, Category, ItemOption, Item, ItemQna, ItemReview
from django_summernote.admin import SummernoteModelAdmin

class CategoryAdmin(admin.ModelAdmin):
	list_display = ['category_id','category_name',]

class BrandAdmin(SummernoteModelAdmin):
	list_display = ['brand_id','brand_name','brand_desc','brand_active',]

class ItemOptionAdmin(admin.ModelAdmin):
	list_display = ['option_id','option_name','option_price','option_custom_price','option_stock',]

class ItemAdmin(SummernoteModelAdmin):
	list_display = ['item_id','item_name','item_desc','price','custom_price','get_categories','brand','get_options_name','image0','delivery','detail',]

class ItemQnaAdmin(SummernoteModelAdmin):
	list_display = ['user','item','secret','question','answer','qna_time',]

class ItemReviewAdmin(SummernoteModelAdmin):
	list_display = ['user','item','score','comment','review_time',]

admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(ItemOption, ItemOptionAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(ItemQna, ItemQnaAdmin)
admin.site.register(ItemReview, ItemReviewAdmin)