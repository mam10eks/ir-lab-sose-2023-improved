FROM ubuntu:22.04

# Add additional dependencies: jupyter so that we can run a notebook directly in the container and jq that we can easily look into the data
RUN apt-get update \
	&& apt-get upgrade -y \
	&& apt-get install -y jq libffi-dev python3 python3-pip python-is-python3 \
	&& pip3 install jupyter ir_datasets \
	&& rm -Rf /var/cache/apt \
	&& rm -Rf /root/.cache/pip

RUN echo "from ir_datasets import datasets_in_progress" >> /usr/local/lib/python3.10/dist-packages/ir_datasets/__init__.py \
	&& mkdir /usr/local/lib/python3.10/dist-packages/ir_datasets/datasets_in_progress \
	&& echo 'from os.path import dirname, basename, isfile, join\nimport glob\nmodules = glob.glob(join(dirname(__file__), "*.py"))\n__all__ = [ basename(f)[:-3] for f in modules if isfile(f) and not f.endswith("__init__.py")]\nfrom . import *\n'  > /usr/local/lib/python3.10/dist-packages/ir_datasets/datasets_in_progress/__init__.py \
	&& pip3 install pandas

# Add code and resources to a directory in the PYTHON_PATH
COPY ir_anthology.py ir-anthology-documents.jsonl topics.xml qrels.txt /usr/local/lib/python3.10/dist-packages/ir_datasets/datasets_in_progress/

