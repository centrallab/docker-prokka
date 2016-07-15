FROM java:8
MAINTAINER a504082002 <a504082002@gmail.com>

# Install dependencies
RUN apt-get update -qq &&\
	apt-get install -yq --no-install-recommends
						git\
						less\
						libdatetime-perl\
						libxml-simple-perl\
						libdigest-md5-perl\
						bioperl &&\
	rm -rf /var/lib/apt/lists/*

# clone prokka
RUN git clone https://github.com/tseemann/prokka.git &&\
	prokka/bin/prokka --setupdb

# set links to /usr/bin
ENV PATH $PATH:/prokka/bin

# set data mounting point
RUN mkdir /data
WORKDIR /data

CMD ["/bin/bash"]

