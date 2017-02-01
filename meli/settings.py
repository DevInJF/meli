ENV= 'PROD' # 'DEV' OR 'PROD'

if ENV == 'PROD':
    from .settings_prod import *
else:
    from .settings_test import *