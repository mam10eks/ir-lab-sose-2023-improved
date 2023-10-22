FROM ubuntu:22.04

# Add additional dependencies: jupyter so that we can run a notebook directly in the container and jq that we can easily look into the data
RUN apt-get update \
	&& apt-get upgrade -y \
	&& apt-get install -y jq libffi-dev python3 python3-pip python-is-python3 openjdk-11-jdk \
	&& pip3 install jupyter ir_datasets \
	&& rm -Rf /var/cache/apt \
	&& rm -Rf /root/.cache/pip \
	&& pip3 install tira python-terrier chatnoir-api \
	&& python3 -c 'import pyterrier as pt; pt.init()'


