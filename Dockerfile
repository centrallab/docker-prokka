FROM java:8-jre-alpine
MAINTAINER a504082002 <a504082002@gmail.com>

# Install dependencies
RUN apk add --update --no-cache git \
	                            less \
	                            gcc \
	                            make \
	                            parallel \
	                            curl \
	                            apkbuild-cpan \
	                            perl-datetime \
	                            perl-xml-parser \
	                            perl-xml-simple \
	                            perl-digest-md5 && \
	cpan -i Bio::Perl && \
	rm -rf /var/cache/apk/* /tmp/* /var/tmp/*

# clone prokka
RUN git clone https://github.com/tseemann/prokka.git && \
    chmod +x /prokka/binaries/linux/* && \
	/prokka/bin/prokka --setupdb
ENV PATH $PATH:/prokka/bin

ADD batch.py /program/batch.py

# set data mounting point
RUN mkdir /data
WORKDIR /data

CMD ["/bin/bash"]

