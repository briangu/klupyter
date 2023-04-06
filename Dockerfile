FROM jupyter/base-notebook:latest

USER root

# Install any system-level dependencies required for your kernel here
# For example, RUN apt-get update && apt-get install -y some-package

# Install your custom kernel
COPY klongpy_kernel /opt/klongpy_kernel
RUN pip install --no-cache-dir /opt/klongpy_kernel && \
    jupyter kernelspec install --user /opt/klongpy_kernel && \
    rm -rf /opt/klongpy_kernel

# Switch back to the non-root user
USER $NB_UID

