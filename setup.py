from setuptools import setup, find_packages

VERSION = "0.0.1"
DESCRIPTION = "Colored prints and inputs"
LONG_DESCRIPTION = "Colored prints and inputs"

# Setting up
setup(
    name="bcolored",
    version=VERSION,
    author="Leonardix007 (Leonardo Ricci)",
    author_email="<leonardoricci775@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'colored text', 'colored', 'colored input'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
