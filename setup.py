# setup.py
from pathlib import Path
from setuptools import find_namespace_packages, setup

# Load packages from requirements.txt
BASE_DIR = Path(__file__).parent
with open(Path(BASE_DIR, "requirements.txt"), "r") as file:
    required_packages = [ln.strip() for ln in file.readlines()]

# setup.py
setup(
    name="spotify-player",
    version=0.1,
    description="A prettier desktop player for Spotify.",
    author="Jacob Rivera",
    author_email="jacobrivera@utexas.edu",
    url="https://github.com/jacobmrivera/spotify-player",
    python_requires=">=3.7",
    install_requires=[required_packages],
)
