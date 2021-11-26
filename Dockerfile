FROM python:3.8.0

RUN git clone --depth=1 https://github.com/Bash-it/bash-it.git ~/.bash_it && \
    bash ~/.bash_it/install.sh --silent

RUN curl -sL https://deb.nodesource.com/setup_12.x | bash - && \
    apt-get upgrade -y && \
    apt-get install -y nodejs && \
    rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip && \
    pip install --upgrade \
    numpy \
    pandas \
    dash \
    Jupyterlab \
    ipywidgets \
    jupyterlab-git \
    jupyter-server-proxy \
    jupyter-dash

RUN jupyter lab build
# RUN pip install --upgrade pip && \
#     pip install --upgrade \
#     jupyterlab "pywidgets>=7.5" 
RUN jupyter labextension install \
    jupyterlab-plotly@4.14.3 \
    @jupyter-widgets/jupyterlab-manager \
    @jupyterlab/git \
    @jupyterlab/server-proxy

COPY entrypoint.sh /usr/local/bin/
RUN chmod 755 /usr/local/bin/entrypoint.sh
COPY config/ /root/.jupyter/

EXPOSE 8888 8050
VOLUME /notebooks
WORKDIR /notebooks
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
# CMD jupyter lab --ip=* --port=8888 --allow-root
