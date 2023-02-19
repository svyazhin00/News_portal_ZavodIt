menu = [{'title':'Главная страница', 'url_name': 'main'},
        {'title':'Популярные новости', 'url_name':'popular'}
        ]


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context['menu'] = menu
        return context
