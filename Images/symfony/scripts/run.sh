#!/bin/bash

chmod 644 /.htaccess
mv /.htaccess $PROJECT_PATH

composer install

php bin/console doctrine:database:create
php bin/console make:migration
php bin/console --no-interaction doctrine:migrations:migrate
# php bin/console --no-interaction doctrine:fixtures:load

/usr/sbin/apache2ctl -D FOREGROUND
