from django.contrib import admin
from .models import Brand, Category, ItemOption, Item, ItemIngredientCombination, ItemQna, ItemReview, RelatedItem, RelatedContent
from django_summernote.admin import SummernoteModelAdmin

class CategoryAdmin(admin.ModelAdmin):
	list_display = ['category_id','category_name',]

class BrandAdmin(SummernoteModelAdmin):
	list_display = ['brand_id','brand_name','brand_desc','brand_active','brand_order',]

class ItemIngredientCombinationInline(admin.TabularInline):
	model = ItemIngredientCombination
	extra = 3
	raw_id_fields = ("ingredient",)

class ItemOptionInline(admin.TabularInline):
	model = ItemOption
	extra = 0

class ItemOptionAdmin(admin.ModelAdmin):
	list_display = ['option_id','option_name','option_price','option_custom_price','option_stock',]

class ItemAdmin(SummernoteModelAdmin):
	list_display = ['item_id','item_active','main1','main2','main3', 'is_sample', 'order_number', 'item_name','item_desc','price','custom_price','get_categories','brand','get_options_name','image0','short_delivery','short_detail']
	inlines = (ItemOptionInline,ItemIngredientCombinationInline,)

class ItemQnaAdmin(SummernoteModelAdmin):
	list_display = ['user','item','secret','question','answer','qna_time',]

class ItemReviewAdmin(SummernoteModelAdmin):
	list_display = ['user','item','score','comment','review_time',]

class RelatedItemAdmin(admin.ModelAdmin):
	list_display = ['item_from','item_to',]

class RelatedContentAdmin(admin.ModelAdmin):
	list_display = ['item_from','content_to_subject','content_to_url','content_to_img']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(ItemOption, ItemOptionAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(ItemQna, ItemQnaAdmin)
admin.site.register(ItemReview, ItemReviewAdmin)
admin.site.register(RelatedItem, RelatedItemAdmin)
admin.site.register(RelatedContent, RelatedContentAdmin)


