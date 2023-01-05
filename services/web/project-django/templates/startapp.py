#!/usr/bin/env python3
import os

APPS = """from django.apps import AppConfig


class {}Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.{}'"""

ADMIN = """from django.contrib import admin"""

MODELS = """from django.db import models"""

VIEWS = """from rest_framework.views import APIView
from rest_framework.response import Response"""

URLS = """from apps.{} import views
from django.urls import path


urlpatterns = [
]"""


def create_file(filepath, content):
    with open(filepath, "w") as f:
        f.write(content)


def scaffold(main_path, name):
    # Core files
    templates = {
        "__init__.py": "",
        "admin.py": ADMIN,
        "apps.py": APPS.format(name.title(), name.lower()),
        "models.py": MODELS,
        "views.py": VIEWS,
        "urls.py": URLS.format(name.lower()),
    }
    for filename, content in templates.items():
        path = os.path.join(main_path, filename)
        with open(path, "w") as f:
            f.write(content)
    # Tests
    path = os.path.join(main_path, "tests")
    os.mkdir(path)
    path = os.path.join(main_path, "tests", "__init__.py")
    with open(path, "w") as f:
        pass
    # Migrations
    path = os.path.join(main_path, "migrations")
    os.mkdir(path)
    path = os.path.join(main_path, "migrations", "__init__.py")
    with open(path, "w") as f:
        pass


def create_app(args):
    try:
        name = args[1]
    except:
        print("startapp requires app name.")
        exit(1)
    base = "apps"
    main_path = os.path.join(base, name)
    if os.path.exists(main_path):
        print("app name already exists, try another name.")
        exit(1)
    os.mkdir(main_path)
    scaffold(main_path, name)
    print(
        f"Add 'apps.{name.lower()}.apps.{name.title()}Config' in INSTALLED_APPS in settings.py"
    )
