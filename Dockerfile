FROM java:8
MAINTAINER a504082002 <a504082002@gmail.com>

# Install dependencies
RUN apt-get update -qq && \
	apt-get install -yq --no-install-recommends \
						git \
						less \
						libdatetime-perl \
						libxml-simple-perl \
						libdigest-md5-perl \
						bioperl && \
	apt-get clean && \
	rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# clone prokka
RUN git clone https://github.com/tseemann/prokka.git && \
	prokka/bin/prokka --setupdb

# set links to /usr/bin
ENV PATH $PATH:/prokka/bin

ADD batch.py /program/batch.py

# set data mounting point
RUN mkdir /data
WORKDIR /data

CMD ["/bin/bash"]

