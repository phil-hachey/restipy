import requests

from jwt_service import JwtService

authSchemeServices = {
    'jwt': JwtService,
    'basic': None
}

class HttpService:
    
    def send(self, request):
        
        auth = request.pop('auth', None)
        auth_type = auth.pop('type', None)
        
        if auth_type and auth_type in authSchemeServices:
            authService = authSchemeServices[auth_type]()
            token = authService.encode(**auth)
            if not ('headers' in request):
                request['headers'] = {}
                
            request['headers']['Authorization'] = token
        
        return requests.get(**request)
