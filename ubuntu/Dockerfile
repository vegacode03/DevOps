# Usa a imagem oficial do Ubuntu
FROM ubuntu:22.04

# Evita prompts interativos
ENV DEBIAN_FRONTEND=noninteractive

# Atualiza o sistema e instala pacotes essenciais
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y \
        sudo \
        curl \
        wget \
        git \
        nano \
        vim \
        unzip \
        python3 \
        python3-pip \
        build-essential \
        && apt-get clean

# Define o diretório padrão
WORKDIR /root

# Comando inicial do container
CMD ["/bin/bash"]
