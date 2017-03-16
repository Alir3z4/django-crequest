import threading

try:
    from django.utils.deprecation import MiddlewareMixin
except ImportError:
    MiddlewareMixin = object


class CrequestMiddleware(MiddlewareMixin):
    """
    Always have access to the current request
    """
    _request = {}

    def process_request(self, request):
        """
        Store request
        """
        self.__class__.set_request(request)

    def process_response(self, request, response):
        """
        Delete request
        """
        self.__class__.del_request()
        return response

    def process_exception(self, request, exception):
        """
        Delete request
        """
        self.__class__.del_request()

    @classmethod
    def get_request(cls, default=None):
        """
        Retrieve request
        """
        return cls._request.get(threading.current_thread(), default)

    @classmethod
    def set_request(cls, request):
        """
        Store request
        """
        cls._request[threading.current_thread()] = request

    @classmethod
    def del_request(cls):
        """
        Delete request
        """
        cls._request.pop(threading.current_thread(), None)
