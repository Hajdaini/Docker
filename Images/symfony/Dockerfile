FROM php:7.3.0-apache-stretch

LABEL maintainer="AJDAINI Hatim <hatim.ajdaini.ext@orange.com>" \
      description="symfony application"

ENV PROJECT_PATH="/var/www/app/"

RUN apt-get update -y && \
    apt-get install -y \
    curl \
    wget \
    git \
    nano \
    unzip \
    && apt-get autoclean

RUN docker-php-ext-install mysqli pdo pdo_mysql

RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

RUN echo "set tabsize 4" >> ~/.nanorc

RUN a2enmod proxy_fcgi ssl rewrite proxy proxy_balancer proxy_http

RUN echo "memory_limit = 512M" >> /usr/local/etc/php/conf.d/docker-php-memlimit.ini

ADD ./apache_config/000-default.conf /etc/apache2/sites-available/000-default.conf

ADD ./apache_config/htaccess /.htaccess

ADD ./scripts/run.sh /run.sh

RUN chmod 770 /run.sh

WORKDIR ${PROJECT_PATH}

CMD ["/run.sh"]
