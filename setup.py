import setuptools
import versioneer


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="zephyr-cfg",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    author="zephyrj",
    author_email="zephyrj@protonmail.com",
    description="A module for managing configuration within python projects.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zephyrj/zephyr-cfg",
    packages=setuptools.find_packages(),
    package_dir={},
    include_package_data=True,
    install_requires=[],
    scripts=[],
    entry_points={},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPL-3.0 License",
        "Operating System :: OS Independent",
    ]
)
