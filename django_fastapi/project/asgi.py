import os
from django.apps import apps
from django.conf import settings
from django.core.wsgi import get_wsgi_application


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
apps.populate(settings.INSTALLED_APPS)


from fastapi import FastAPI
from fastapi.middleware.wsgi import WSGIMiddleware
from starlette.middleware.cors import CORSMiddleware
from api.endpoints import api_router

def get_application() -> FastAPI:
    """
    :desc:
    FastAPI instance 를 가져온 다음 middle ware 를 추가하고 API router 를 설정해서
    """

    app = FastAPI(title=settings.PROJECT_NAME, debug=settings.DEBUG)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.ALLOWED_HOSTS or ["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.include_router(api_router, prefix="/api")
    app.mount("/django", WSGIMiddleware(get_wsgi_application()))

    return app


app = get_application()
