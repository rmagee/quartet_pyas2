from .services import RouteFiles

class QuartetAS2Middleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        if request.META["PATH_INFO"]=='/pyas2/as2receive':
           data = {
               'organization':request.META["HTTP_AS2_FROM"],
               'partner': request.META["HTTP_AS2_TO"],
               'message_id': request.META["HTTP_MESSAGE_ID"]
           }

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

