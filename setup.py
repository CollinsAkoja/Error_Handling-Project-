from setuptools import setup, find_packages

setup(
    name="api_error_handling",
    version="0.1.0",
    description="Production-ready API error handling for Flask and FastAPI",
    packages=find_packages("src"),
    package_dir={"": "src"},
    install_requires=[
        "Flask>=2.0",
        "fastapi>=0.110",
        "uvicorn[standard]>=0.24",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
