from typing import Any
from django import forms
from .models import review
from django.core.exceptions import ValidationError


class AddReviewForm(forms.Form):  # определяю форму

    title = forms.CharField(max_length=review.TITLE_MAX_LENGTH, label="Title")
    content = forms.CharField(widget=forms.Textarea, label="Content")
    post_type = forms.ChoiceField(choices=review.POST_TYPES, label="Review type")
    image = forms.ImageField(label="Main image")

    def clean_title(self):  # добавил метод очистки
        title_data = self.cleaned_data["title"]  # получаю очищенные данные заголовка
        title_data = format_text_value(title_data)

        if title_data == "admin":
            raise ValidationError("Please enter not a admin value")

        return title_data

    def clean_content(self):  # добавил метод очистки
        content_data = self.cleaned_data[
            "content"
        ]  # получаю очищенные данные содержания
        content_data = format_text_value(content_data)

        content_data = content_data.strip().lower()

        if content_data == "admin":
            raise ValidationError("Please enter not a admin value")

        try:
            title_data = self.cleaned_data[
                "title"
            ]  # пытаюсь получить очищенные данные заголовка
        except KeyError:
            raise ValidationError(
                "Please fill title with a correct value"
            )  # ошибка если заголовок не заполнен

        if content_data == title_data:  # проверка совпадения заголовка с содержанием
            raise ValidationError(
                "Content cannot has the same value as title"
            )  # ошибка если совпадает

        return content_data


def format_text_value(value):
    return value.strip().lower()


class AddReviewModelForm(forms.ModelForm):

    class Meta:
        model = review
        fields = ("title", "content", "post_type", "image")
