FROM java:8
MAINTAINER a504082002 <a504082002@gmail.com>

# Install dependencies
RUN apt-get update -qq &&\
	apt-get install -yq git\
						less\
						libdatetime-perl\
						libxml-simple-perl\
						libdigest-md5-perl\
						bioperl

# clone prokka
RUN git clone https://github.com/tseemann/prokka.git &&\
	prokka/bin/prokka --setupdb

# set links to /usr/bin
RUN ln -s /prokka/bin/* /usr/bin

# set data mounting point
RUN mkdir /data

CMD ["/bin/bash"]

