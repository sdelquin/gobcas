from prettyconf import config

APP_SECRET = config('APP_SECRET')

CAS_SERVER = config('CAS_SERVER')
CAS_LOGIN_ROUTE = config('CAS_LOGIN_ROUTE', default='/login')
CAS_LOGOUT_ROUTE = config('CAS_LOGOUT_ROUTE', default='/logout')
CAS_VALIDATE_ROUTE = config('CAS_VALIDATE_ROUTE', default='/serviceValidate')
