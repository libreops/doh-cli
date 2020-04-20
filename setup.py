from setuptools import setup
from doh_cli import __version__


def readme_md():
    """Return contents of README.md"""
    return open("README.md").read()


def changelog_md():
    """Return contents of Changelog.md"""
    return open("Changelog.md").read()


setup(
    name="doh-cli",
    version=__version__,
    author="LibreOps",
    author_email="team@libreops.cc",
    url="https://gitlab.com/libreops/doh-cli",
    description="a simple DNS-over-HTTPS client",
    long_description_content_type="text/markdown",
    long_description=readme_md() + "\n\n" + changelog_md(),
    include_package_data=True,
    zip_safe=False,
    license="LICENSE",
    install_requires=[
        "dnspython",
        "requests"
    ],
    packages=["doh_cli"],
    scripts=["bin/doh-cli"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Internet :: Name Service (DNS)",
    ]
)
