from datetime import datetime

class BaseMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

class ProcessViewNoneMiddleware(BaseMiddleware):
  ### process_view gets called before the view gets called
    def process_view(self, request, view_func, view_args, view_kwargs):
        print('----- Middleware view %s' % view_func.__name__ % view_args % view_kwargs)
        print("My middleware works breh")
        return None

class TestGraphQLMiddleWare(object):
    def resolve(self, next, root, info, **args):
        print("Running middleware...")
        return next(root, info, **args)