import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example-pkg-edouard-lopez",
    version="1.2.0",
    author="Édouard Lopez",
    author_email="contact@edouard-lopez.com",
    description="Pretty, minimal and fast cross-shell prompt",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/edouard-lopez/pure",
    packages=setuptools.find_packages(),
    classifiers=[
        'Topic :: System :: Shells',
        "Operating System :: OS Independent",
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Operating System :: POSIX',
        'Natural Language :: English',
        'Topic :: Terminals',
        'Environment :: Console',
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)