# Use NVIDIA PyTorch as the base image
FROM nvcr.io/nvidia/pytorch:23.12-py3

# Set environment variables for Miniconda and Conda environment
ENV CONDA_DIR /opt/conda
ENV PATH $CONDA_DIR/bin:$PATH

# Install Miniconda
RUN apt-get update && apt-get install -y wget && \
    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh && \
    bash Miniconda3-latest-Linux-x86_64.sh -b -p $CONDA_DIR && \
    rm Miniconda3-latest-Linux-x86_64.sh

# Create a new Conda environment named "bocr" with Python 3.9
RUN conda create -n bocr python=3.9 -y

RUN conda activate bocr

# # Clone BharatOCR repository
# RUN git clone https://github.com/Bhashini-IITJ/BharatOCR.git && \
#     cd BharatOCR && \
#     git switch requirements && \
#     python setup.py sdist bdist_wheel && \
#     pip install ./dist/bharatOCR-1.0.2-py3-none-any.whl[cu118] --extra-index-url https://download.pytorch.org/whl/cu118

# # Install additional dependencies
# RUN apt-get update && apt-get install -y ffmpeg libsm6 libxext6

# # Set default command to run BharatOCR
# CMD ["conda", "run", "-n", "bocr", "python", "-m", "bharatOCR.ocr"]
