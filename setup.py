from setuptools import setup, find_packages

setup(
    name="recommend_llm",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "uvicorn"
    ],
    description="recommend_llm service for Django and FastAPI",
    author="hyeilly",
    author_email="dev.jiine@gmail.com",
    url="https://github.com/hyeilly/recommend-llm@release/django",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10',
)
