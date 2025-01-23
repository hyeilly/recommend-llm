from setuptools import setup, find_packages

setup(
    name="recommend-llm",
    version="0.1",
    packages=find_packages(include=["endpoints.*"]),
    install_requires=[
        "fastapi",
        "uvicorn",
    ]
)
