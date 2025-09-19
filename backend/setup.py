from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()
long_description = (here.parent / "README.md").read_text(encoding="utf-8")

setup(
    name="ai-image-caption-backend",
    version="0.1.0",
    description="FastAPI backend for AI Image Caption Generator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="edgar",
    author_email="edgarmcochieng@gmail.com",
    url="https://github.com/49ochieng/ai-image-caption-generator",
    license="MIT",
    packages=find_packages(),
    install_requires=[
        "fastapi",
        "uvicorn",
        "python-multipart"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Framework :: FastAPI"
    ],
    python_requires=">=3.8",
)