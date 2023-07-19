from setuptools import setup
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

REPO_NAME = "Cities-Recommendation-System-using-Machine-Learning"
AUTHOR_USERNAME = "SemalJohari"
SRC_REPO = "src"
LIST_OF_REQUIREMENTS = ['streamlit', 'numpy']

setup(
    name=SRC_REPO,
    version="0.0.1",
    author=AUTHOR_USERNAME,
    description="A small package for City Recommendation System",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USERNAME}/{REPO_NAME}",
    author_email="semaljohari80@gmail.com",
    packages=[SRC_REPO],
    license="MIT",
    python_requires=">=3.7",
    install_requires=LIST_OF_REQUIREMENTS
)