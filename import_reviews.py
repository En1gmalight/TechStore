import os
import django
from datetime import datetime


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "TechStore.settings")
django.setup()

from main.models import Author, review


author_john = Author.objects.create(name="John Doe", email="john.doe@gmail.com")
author_emily = Author.objects.create(name="Emily Davis", email="emily.davis@example.com")
author_michael = Author.objects.create(name="Michael Brown", email="michael.brown@mail.com")
author_david = Author.objects.create(name="David Wilson", email="david.wilson@gmail.com")
author_jane = Author.objects.create(name="Jane Smith", email="jane.smith@example.com")


review_1 = review.objects.create(
    title="Amazing Battery Life",
    content="I recently bought the iPhone 15 Pro Max, and I am amazed by its battery life. It lasts all day with heavy usage. Highly recommend!",
    post_type="p",
    issued=datetime(2024, 8, 30, 10, 0),
    author=author_john,
)

review_2 = review.objects.create(
    title="Beautiful Display",
    content="The display on the iPhone 15 is stunning. Colors are vibrant, and the resolution is top-notch. Watching videos is a delight.",
    post_type="p",
    issued=datetime(2024, 9, 2, 16, 0),
    author=author_emily,
)

review_3 = review.objects.create(
    title="Smooth Performance",
    content="I've been using the iPhone 13 for a few months now, and its performance is incredibly smooth. No lags or glitches. Very satisfied!",
    post_type="p",
    issued=datetime(2024, 9, 1, 14, 0),
    author=author_michael,
)

review_4 = review.objects.create(
    title="User-Friendly Interface",
    content="The iPhone 14 has a very user-friendly interface. It's easy to navigate, and the new features are intuitive. Great job, Apple!",
    post_type="p",
    issued=datetime(2024, 9, 3, 18, 0),
    author=author_david,
)

review_5 = review.objects.create(
    title="Great Camera Quality",
    content="The camera on the iPhone 14 Pro is fantastic. The photos are crisp and clear, even in low light. Perfect for photography enthusiasts.",
    post_type="p",
    issued=datetime(2024, 8, 31, 12, 0),
    author=author_jane,
)
