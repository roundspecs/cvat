# local-settings.py  –  CSRF / host overrides for dev tunneling
from cvat.settings.production import *

# Trust the dynamic Pinggy sub‑domain and any local host
CSRF_TRUSTED_ORIGINS = ['https://*.pinggy.link'] # Use your domain name explicitly if needed
ALLOWED_HOSTS = ['*']