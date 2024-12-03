from setuptools import setup, find_packages

setup(
    name="IndicPhotoOCR",
    version="1.2.0",
    description="Scene Text Recognition Toolkit across 13 Indian Languages which contains detection, script identification, and text recognition modules",
    long_description=open("README.md").read() + "\n\n" + open("CHANGELOG.md").read(),
    long_description_content_type="text/markdown",
    author="Anik De",
    author_email="anekde@gmail.com",
    url="https://github.com/Bhashini-IITJ/IndicPhotoOCR",
    packages=find_packages(),
    python_requires='>=3.9',
    install_requires=[
        # Your mandatory dependencies here
        'aiohappyeyeballs==2.4.3',
        'aiohttp==3.10.11',
        'aiosignal==1.3.1',
        'async-timeout==4.0.3',
        'attrs==24.2.0',
        'certifi==2024.8.30',
        'charset-normalizer==3.4.0',
        'click==8.1.7',
        'filelock==3.16.1',
        'frozenlist==1.5.0',
        'fsspec==2024.10.0',
        'huggingface-hub==0.26.1',
        'idna==3.10',
        'jinja2==3.1.4',
        'joblib==1.4.2',
        'lightning-utilities==0.11.8',
        'markupsafe==3.0.2',
        'mpmath==1.3.0',
        'multidict==6.1.0',
        'networkx==3.2.1',
        'nltk==3.9.1',
        'numpy==1.26.4',
        'packaging==24.1',
        'pillow==11.0.0',
        'propcache==0.2.0',
        'pytorch-lightning==2.4.0',
        'pyyaml==6.0.2',
        'regex==2024.9.11',
        'requests==2.32.3',
        'safetensors==0.4.5',
        'sympy==1.13.1',
        'timm==1.0.11',
        'torchmetrics==1.5.1',
        'tqdm==4.66.5',
        'typing-extensions==4.12.2',
        'urllib3==2.2.3',
        'yarl==1.16.0',
        'opencv-python==4.10.0.84',
        'shapely==2.0.6',
        'openai-clip==1.0.1',
        'lmdb==1.5.1',
        'easydict==1.13',
        'scipy==1.13.1',
        'six==1.16.0',
        'matplotlib==3.9.0'

    ],
    extras_require={
        'cu118': [
            'torch==2.5.0+cu118',
            'torchvision==0.20.0+cu118',
            # Any additional packages specific to cu118
        ],
        'cu121': [
            'torch==2.5.0+cu121',
            'torchvision==0.20.0+cu121',
            # Any additional packages specific to cu121
        ],
        'cpu': [
            'torch==2.5.0',
            'torchvision==0.20.0',
            # Any additional packages specific to CPU
        ],
    },
)
