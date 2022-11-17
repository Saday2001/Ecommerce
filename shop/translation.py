from dataclasses import fields
from modeltranslation.translation import register,TranslationOptions
from .models import *

@register(Gender)

class Gendertranslation(TranslationOptions):
    fields = ('title')

@register(Category)

class CategoryTranslation(TranslationOptions):
    fields = ('title')

@register(Subb_category)

class SubcategoryTranslation(TranslationOptions):
    fields = ('title')

@register(Color)

class ColorTranslation(TranslationOptions):
    fields = ('title')