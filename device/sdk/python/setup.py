import setuptools

setuptools.setup(
    name="SecAutoBan",
    version="0.0.1",
    author="SecReport",
    author_email="sec-report@outlook.com",
    description="SecAutoBan SDK",
    long_description="SecAutoBan SDK",
    long_description_content_type="text/markdown",
    url="https://github.com/sec-report/SecAutoBan",
    packages=setuptools.find_packages(),
    install_requires = ["pycryptodome", "websocket-client"]
)