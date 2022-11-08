from django.shortcuts import render, redirect
from pages.utils import user_authorized_items, user_unauthorized_items


def index(request):
    # return redirect('accounts-profile')
    menu_context = {
        'user_items': user_authorized_items if request.user.is_authenticated else user_unauthorized_items
    }
    menu_context.update({'title': 'Metaperson', 'current_page': 'home'})
    return render(request, 'pages/index.html', context=menu_context)
