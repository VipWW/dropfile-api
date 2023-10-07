from setuptools import find_packages, setup

setup(
    name="DropFile",
    version="0.1",
    description="DropFile - alternative to DropBox",
    python_requires=">=3.10, <4",
    packages=find_packages(include=["app", "app.*"]),
    install_requires=[
        "python-dotenv",
        "flask[async]",
        "flask-cors",
        "webargs",
        "flask-sqlalchemy",
        "flask-marshmallow",
        "marshmallow-sqlalchemy",
        "marshmallow",
        "flask_login",
        "black",
        "autopep8",
        "psycopg2-binary",
    ],
)
