from catalog.models import Product
from search.models import SearchTerm
from django.db.models import Q
from stats import stats

STRIP_WORDS =['a','an','and','by','for','from','in','no',
              'not','of','on','or','that','the','to','with','there','those']

#store the search text in the database
def store(request, word):
    if len(word) > 2:
        term = SearchTerm()
        term.word = word
        term.ip_address = request.META.get('REMOTE_ADDR')
        term.user = None
        term.tracking_id = stats.tracking_id(request)
        if request.user.is_authenticated:
            term.user = request.user
        term.save()

#get products marching the search text
def products(search_text):
    words = _prepare_words(search_text)
    products = Product.active.all()
    results = {}
    results['products'] = []
    for word in words:
        products = products.filter(Q(name__icontains=word)|
                                   Q(description__icontains=word)|
                                   Q(sku__iexact=word)|
                                   Q(brand__icontains=word)|
                                   Q(meta_description__icontains=word)|
                                   Q(meta_keywords__icontains=word))
        results['products'] = products
    return results
#remove out common words, limit to 5 words
def _prepare_words(search_text):
    words = search_text.split()
    for common_word in STRIP_WORDS:
        if common_word in words:
            words.remove(common_word)
    return words[0:5]
