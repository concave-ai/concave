FROM python:3.9

RUN apt update && apt install -y \
npm \
nodejs \
wget \
git \
build-essential \
libffi-dev \
libtiff-dev \
python3 \
python3-pip \
python-is-python3 \
jq \
curl \
locales \
locales-all \
python3-setuptools \
tzdata

RUN npm install -g @sourcegraph/scip-python

WORKDIR /workspace
RUN git clone https://github.com/astropy/astropy app

WORKDIR /workspace/app
RUN git checkout d16bfe05a744909de4b27f5875fe0d4ed41ce607



RUN sed -i 's/requires = \["setuptools",/requires = \["setuptools==68.0.0",/' pyproject.toml && \
    \
    \
    pip install attrs==23.1.0 exceptiongroup==1.1.3 execnet==2.0.2 hypothesis==6.82.6 iniconfig==2.0.0 numpy==1.25.2 packaging==23.1 pluggy==1.3.0 psutil==5.9.5 pyerfa==2.0.0.3 pytest-arraydiff==0.5.0 pytest-astropy-header==0.2.2 pytest-astropy==0.10.0 pytest-cov==4.1.0 pytest-doctestplus==1.0.0 pytest-filter-subpackage==0.1.2 pytest-mock==3.11.1 pytest-openfiles==0.5.0 pytest-remotedata==0.4.0 pytest-xdist==3.3.1 pytest==7.4.0 PyYAML==6.0.1 setuptools==68.0.0 sortedcontainers==2.4.0 tomli==2.0.1 \
    && python -m pip install -e .[test] --verbose


RUN scip-python index . --project-name=pytest && \
    mkdir -p /workspace/index/scip && mv index.scip /workspace/index/scip/

CMD ["sleep", "900"]