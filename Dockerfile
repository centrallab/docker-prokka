FROM ubuntu:latest
MAINTAINER a504082002 <a504082002@gmail.com>

# Install dependencies
RUN apt-get update -qq &&\
	apt-get install -yq git\
						libdatetime-perl\
						libxml-simple-perl\
						libdigest-md5-perl\
						bioperl

# clone prokka
RUN git clone https://github.com/tseemann/prokka.git &&\
	prokka/bin/prokka --setupdb

# set environment variables
ENV $PATH=$PATH:prokka/bin

CMD ["/bin/bash"]

