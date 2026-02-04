from django.shortcuts import render
import random

# Quotes by ONE person (example: Albert Einstein)
QUOTES = [
    "Life is like riding a bicycle. To keep your balance you must keep moving.",
    "Imagination is more important than knowledge.",
    "Strive not to be a success, but rather to be of value."
]

# USE DIRECT IMAGE FILES (NOT Wikipedia pages)
IMAGES = [
    "https://upload.wikimedia.org/wikipedia/commons/d/d3/Albert_Einstein_Head.jpg",
    "https://img.goodfon.com/original/2560x1600/5/5f/albert-einstein-albert-6866.jpg",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTACzE5HV0kLGapGGZUqWGAkzPwmVGPJc6oRg&s"
]

def quote(request):
    context = {
        'quote': random.choice(QUOTES),
        'image': random.choice(IMAGES)
    }
    return render(request, 'quotes/quote.html', context)

def show_all(request):
    context = {
        'quotes': QUOTES,
        'images': IMAGES
    }
    return render(request, 'quotes/show_all.html', context)

def about(request):
    return render(request, 'quotes/about.html')
