from django.contrib import admin
from django import forms
from .models import CategoryRoom, Room, Booking

# Список доступных удобств
AVAILABLE_AMENITIES = [
    "Wi-Fi",
    "Кондиционер",
    "Телевизор",
    "Холодильник",
    "Сейф",
]


class CategoryRoomAdminForm(forms.ModelForm):
    # Перекрываем поле amenities для кастомного отображения
    amenities = forms.MultipleChoiceField(
        choices=[(amenity, amenity) for amenity in AVAILABLE_AMENITIES],
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Удобства",
    )

    class Meta:
        model = CategoryRoom
        fields = "__all__"

    def clean_amenities(self):
        # Преобразуем список выбранных значений в JSON-совместимый формат
        return self.cleaned_data["amenities"]


class CategoryRoomAdmin(admin.ModelAdmin):
    form = CategoryRoomAdminForm


admin.site.register(CategoryRoom, CategoryRoomAdmin)
admin.site.register(Room)
admin.site.register(Booking)