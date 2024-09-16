from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="igsm",  # Changed to lowercase
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A generator for Infinite Grade School Math (igsm) datasets",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kaminocode/igsm",
    packages=find_packages(exclude=["tests*"]),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.7",
    install_requires=[
        "pyyaml>=5.3.1",
        "numpy>=1.19.0",
    ],
    extras_require={
        "dev": [
            "pytest>=6.2.5",
            "pytest-cov>=2.12.1",
            "black>=21.9b0",
            "isort>=5.9.3",
            "flake8>=3.9.2",
        ],
    },
    include_package_data=True,
    package_data={
        "igsm": ["knowledge_base/*.yaml", "knowledge_base/categories/*.yaml"],  # Changed to lowercase
    },
)