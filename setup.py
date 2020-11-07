import setuptools

setuptools.setup(
    name = "nsfw",
    version = "1.0.0",
    author = "sirius demon",
    author_email = "mory2016@126.com",
    maintainer = "ashing zhang",
    maintainer_email = "2415199241@qq.com",
    description="nsfw in onnx",
    long_description="I wish everyone become happy and full of wisdom",
    long_description_content_type='text/markdown',
    url = "https://github.com/siriusdemon/deep-first-aid",
    packages=setuptools.find_packages(),
    package_data = {
        'nsfw': ['model.onnx'],
    },
    classifiers = [
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)