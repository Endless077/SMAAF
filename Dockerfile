# ============================================================
# Dockerfile - Static Malware Analysis Automation Framework
# Base image: Ubuntu 24.04 (Noble)
# ============================================================

FROM ubuntu:24.04

LABEL maintainer="user"
LABEL project="Static Malware Analysis Automation Framework"
LABEL description="Container for static malware analysis all-in-one."

# ------------------------------------------------------------
# Environment configuration
# ------------------------------------------------------------
ENV TZ=Etc/UTC
ENV LANG=C.UTF-8
ENV LC_ALL=C.UTF-8
ENV PYTHONUNBUFFERED=1
ENV DEBIAN_FRONTEND=noninteractive

# ------------------------------------------------------------
# System dependencies & analysis tools
# ------------------------------------------------------------
RUN apt-get update && apt-get install -y --no-install-recommends \
    automake bison binutils build-essential \
    ca-certificates cmake curl file flex \
    git gradle htop iputils-ping jq \
    less libarchive-dev libfuzzy-dev libmagic-dev libmagic1 \
    libtool libyara-dev locales lsof nano \
    net-tools openjdk-21-jdk-headless p7zip-full pkg-config python3 \
    python3-dev python3-pip python3-venv tar tcpdump \
    tree unrar-free unzip upx vim \
    wget xz-utils yara zip zstd \
    && rm -rf /var/lib/apt/lists/*

# ------------------------------------------------------------
# Ghidra
# ------------------------------------------------------------
ENV GHIDRA_VERSION=11.4.2
ENV GHIDRA_BUILD=20250826
ENV GHIDRA_HOME=/opt/ghidra

RUN wget -q https://github.com/NationalSecurityAgency/ghidra/releases/download/Ghidra_${GHIDRA_VERSION}_build/ghidra_${GHIDRA_VERSION}_PUBLIC_${GHIDRA_BUILD}.zip -O /tmp/ghidra.zip \
    && unzip /tmp/ghidra.zip -d /opt \
    && mv /opt/ghidra* /opt/ghidra \
    && rm -rf /tmp/ghidra.zip

ENV PATH="${PATH}:${GHIDRA_HOME}"
ENV JAVA_HOME=/usr/lib/jvm/java-21-openjdk-amd64

# ------------------------------------------------------------
# radare2
# ------------------------------------------------------------
RUN git clone --depth 1 https://github.com/radareorg/radare2.git /tmp/radare2 \
    && cd /tmp/radare2 \
    && ./configure --prefix=/opt/radare2 \
    && make -j"$(nproc)" && make install \
    && echo "/opt/radare2/lib" > /etc/ld.so.conf.d/radare2.conf \
    && ldconfig \
    && rm -rf /tmp/radare2

ENV PATH="${PATH}:/opt/radare2/bin"

# ------------------------------------------------------------
# Application setup
# ------------------------------------------------------------
WORKDIR /app
COPY . /app

# Create isolated virtual environment
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:${PATH}"

# Upgrade pip and install Python dependencies
RUN pip install --no-cache-dir --upgrade pip setuptools wheel \
 && pip install --no-cache-dir -r requirements.txt

# ------------------------------------------------------------
# APIs port exposition and default command
# ------------------------------------------------------------
EXPOSE 8000
CMD ["/bin/bash"]
