from django.shortcuts import render, redirect
import datetime
from .models import iPhoneCategory, iPhoneModel, Author, review
from django.http import HttpResponse, HttpResponseNotFound
from .forms import AddReviewForm, AddReviewModelForm
from django.core.mail import send_mail
import requests

# Create your views here


def home_page(request):
    return render(request, "home.html")


def iphones_page(request):
    iphones_15 = iPhoneModel.objects.filter(category__name="iPhone 15/Plus/Pro/Pro Max")
    iphones_14 = iPhoneModel.objects.filter(category__name="iPhone 14/Plus/Pro/Pro Max")
    iphones_13 = iPhoneModel.objects.filter(category__name="iPhone 13/mini/Pro/Pro Max")

    print(f"iPhones 15 Count: {iphones_15.count()}")
    print(f"iPhones 14 Count: {iphones_14.count()}")
    print(f"iPhones 13 Count: {iphones_13.count()}")

    return render(
        request,
        "iphones.html",
        {"iphones_15": iphones_15, "iphones_14": iphones_14, "iphones_13": iphones_13},
    )


def about_page(request):
    return render(request, "about.html")


def all_reviews_page(request):
    reviews = review.objects.all()
    return render(request, "reviews.html", {"reviews": reviews})


def review_detail_page(request, review_id):
    try:
        r = review.objects.get(id=review_id)  # пытаюсь получить отзыв по id
    except review.DoesNotExist:
        return HttpResponseNotFound(f"The review with id {review_id} does not exist")
    return render(request, "review_detail.html", {"review": r})


def callback_request_page(request):
    return render(request, "callback_request.html")


def submit_form(request):
    if request.method == "POST":
        name = request.POST["name"]  # получаю имя и телефон
        phone = request.POST["phone"]

        send_mail(
            "New Callback Request",
            f"Name: {name}\nPhone: {phone}",
            "bancher85@gmail.com",
            ["tehnikalux.by@gmail.com"],
            fail_silently=False,
        )

        telegram_token = "6254704509:AAHMwzvy2PeBoeqP-39y0xfELw1CL_QdW3I"
        chat_id = "5997319370"
        message = f"New Callback Request\nName: {name}\nPhone: {phone}"
        requests.post(
            f"https://api.telegram.org/bot{telegram_token}/sendMessage",
            data={"chat_id": chat_id, "text": message},
        )

        return redirect("callback_request_page")
    return render(request, "home.html")  # если запрос не POST


def add_reviews_page(request):

    if request.method == "POST":
        form = AddReviewForm(
            request.POST, request.FILES
        )  # создаю форму с данными из post запроса и файла

        if form.is_valid():  # проверяем, валидна ли форма
            review_entry = review()  # новый экземпляр модели review
            review_entry.author = Author.objects.all()[0]
            review_entry.issued = datetime.datetime.now()
            review_entry.title = form.cleaned_data[
                "title"
            ]  # устанавливаю заголовок отзыва из очищенных данных формы
            review_entry.content = form.cleaned_data["content"]
            review_entry.post_type = form.cleaned_data["post_type"]
            review_entry.image = form.cleaned_data["image"]
            review_entry.save()

            return redirect("review_detail_page", review_entry.id)

    else:
        form = AddReviewForm()
    return render(request, "add_review.html", {"form": form})


# def add_reviews_page(request):
#     if request.method == "POST":
#         form = AddReviewModelForm(request.POST, request.FILES)

#         if form.is_valid():
#             review_entry = form.save(commit=False)
#             review_entry.author = Author.objects.all()[0]
#             review_entry.issued = datetime.datetime.now()

#             form.save()
#             form.save_m2m()  # сохраняю многие ко многим отношения

#             return redirect("review_detail_page", review_entry.id)

#     else:
#         form = AddReviewModelForm()
#     return render(request, "add_review.html", {'form':form})
