from rest_toolkit import resource


@resource(route_path='/')
class Resource(object):
    def __init__(self, request):
        pass


@Resource.controller('engage')
def engage(resource, request):
    return {'message': 'Ai ai captain'}
