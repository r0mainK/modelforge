from importlib.machinery import SourceFileLoader
from pathlib import Path

from setuptools import find_packages, setup

root = Path(__file__).parent
modelforge = SourceFileLoader(
    "modelforge", (root / "modelforge" / "version.py").as_posix()
).load_module()
with (root / "README.md").open(encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="modelforge",
    description="APIs and tools to work with abstract 'models' - files "
    "with numpy arrays and metadata. It is possible to publish "
    "models, list them. There is a built-in cache. Storage has backends.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    version=modelforge.__version__,
    license="Apache 2.0",
    author="source{d}",
    author_email="machine-learning@sourced.tech",
    url="https://github.com/src-d/modelforge",
    download_url="https://github.com/src-d/modelforge",
    packages=find_packages(exclude=("modelforge.tests",)),
    keywords=[
        "model",
        "git",
        "asdf",
        "gcs",
        "google cloud storage",
        "machine learning",
        "registry",
    ],
    install_requires=[
        "asdf>=2.4.0,<2.5",
        "lz4>=1.0,<3.0",
        "numpy>=1.12,<2.0",
        "scipy>=1.0,<2.0",
        "clint>=0.5.0,<0.6",
        "google-cloud-storage>=1.2,<=1.2.0",
        # dulwich does not specify an upper version constraint for urllib3
        # so we may end up with a conflict otherwise
        "urllib3<1.25",
        "requests>=2.0,<3.0",
        "dulwich>=0.19,<1.0",
        "jinja2>=2.10.1,<3.0",
        "humanize>=0.5.0,<0.6",
        "python-dateutil>=2.0,<3.0",
        "typing;python_version<'3.5'",
        "pygtrie>=1.0,<3.0",
        "xxhash>=1.0,<2.0",
        "spdx>=2.0,<3.0",
    ],
    entry_points={"console_scripts": ["modelforge=modelforge.__main__:main"]},
    package_data={"": ["LICENSE", "README.md"], "modelforge": ["templates/*"]},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Libraries",
    ],
)
