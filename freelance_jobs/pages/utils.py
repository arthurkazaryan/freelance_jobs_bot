class DataMixin:

    def get_user_context(self, **kwargs):
        context = kwargs
        context['user_items'] = user_unauthorized_items if not self.request.user.is_authenticated \
            else user_authorized_items

        return context


user_unauthorized_items = [{'title': 'Sign Up', 'url_name': 'accounts-register'},
                           {'title': 'Log In', 'url_name': 'accounts-login'}]
user_authorized_items = [{'title': 'Profile', 'url_name': 'accounts-profile'},
                         {'title': 'Logout', 'url_name': 'accounts-logout'}]
