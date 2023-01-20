from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from .models import Product
from carts.cart import Cart
from .forms import CommentForms
from carts.forms import AddToCartProductForm


def ProductListView(request):
    cart = Cart(request)
    product = Product.objects.all()
    paginator = Paginator(product, 12)  # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'shop/product_list.html', {'products': product, 'cart': cart, 'page_obj': page_obj})


def Details_view(request, pk):
    # get book object
    product = get_object_or_404(Product, pk=pk)
    product_comments = product.comments.all()
    product_form = AddToCartProductForm()
    cart = Cart(request)
    if request.method == 'POST':
        comment_form = CommentForms(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.product = product
            new_comment.user = request.user  # username login User
            new_comment.save()
            comment_form = CommentForms()
    else:
        comment_form = CommentForms()

    return render(request, 'shop/product_detail.html', {'product': product,
                                                        'comments': product_comments,
                                                        'comment_form': comment_form,
                                                        'product_form': product_form,
                                                        'cart': cart,
                                                        })

