from setuptools import setup, find_packages

setup(
    name="recommend_llm",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "fastapi",
        "uvicorn",
    ]
)
