FROM jupyter/base-notebook:latest

USER root

# Install any system-level dependencies required for your kernel here
# For example, RUN apt-get update && apt-get install -y some-package

# Install your custom kernel
COPY . /opt/klupyter

# Set the appropriate permissions for .local and .ipython directories
RUN mkdir -p /home/${NB_USER}/.local && \
    mkdir -p /home/${NB_USER}/.ipython && \
    chown -R ${NB_UID}:users /home/${NB_USER}/.local && \
    chmod -R 755 /home/${NB_USER}/.local && \
    chown -R ${NB_UID}:users /home/${NB_USER}/.ipython && \
    chmod -R 755 /home/${NB_USER}/.ipython && \
    chown -R ${NB_UID}:users /opt/klupyter

# Switch back to the non-root user
USER ${NB_UID}

# Install your custom kernel
RUN cd /opt/klupyter && \
    pip3 install -e . && \
    jupyter kernelspec install --user klongpy_kernel
