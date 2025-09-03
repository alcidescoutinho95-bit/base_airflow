FROM jupyter/pyspark-notebook:spark-3.4.1

USER root

COPY requirements.txt /tmp/requirements.txt

RUN pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt
    
USER $NB_UID
