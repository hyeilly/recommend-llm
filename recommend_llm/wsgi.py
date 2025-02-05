import os
from app.recommend_llm.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.recommend_llm.settings')

application = get_wsgi_application()