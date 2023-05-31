from distutils.core import setup
import pathlib

ROOT = pathlib.Path(__file__).parent
with open(ROOT / "README.md", "r", encoding="utf-8") as f:
    README = f.read()
__version__ = __import__("disnake_debug.__init__").__version__

setup(
    name="disnake_debug",
    packages=["disnake_debug", "disnake_debug.dialogs"],
    version=__version__,
    license="MIT",
    description=("A visual debugging extension for disnake discord bots;" "blacklisting, evaluation, echoing and more"),
    long_description=README,
    long_description_content_type="text/markdown",
    author="Caeden PH",
    author_email="caedenperelliharris@gmail.com",
    url="https://github.com/CaedenPH/disnake_debug",
    download_url=f'https://github.com/CaedenPH/disnake_debug/archive/refs/tags/v_{__version__.replace(".", "")}.tar.gz',
    keywords=["disnake", "discord", "debugging", "visual", "extension", "cog"],
    project_urls={
        "Code": "https://github.com/CaedenPH/disnake_debug",
    },
    install_requires=[
        "disnake",
        "aiosqlite",
        "fuzzywuzzy",
        "python-Levenshtein",
        "python-dotenv",
        "disnake-paginator",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
