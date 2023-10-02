Apache + mod-wsgi configuration
===============================

An example Apache2 vhost configuration follows::

    WSGIDaemonProcess bobvance-<target> threads=5 maximum-requests=1000 user=<user> group=staff
    WSGIRestrictStdout Off

    <VirtualHost *:80>
        ServerName my.domain.name

        ErrorLog "/srv/sites/bobvance/log/apache2/error.log"
        CustomLog "/srv/sites/bobvance/log/apache2/access.log" common

        WSGIProcessGroup bobvance-<target>

        Alias /media "/srv/sites/bobvance/media/"
        Alias /static "/srv/sites/bobvance/static/"

        WSGIScriptAlias / "/srv/sites/bobvance/src/bobvance/wsgi/wsgi_<target>.py"
    </VirtualHost>


Nginx + uwsgi + supervisor configuration
========================================

Supervisor/uwsgi:
-----------------

.. code::

    [program:uwsgi-bobvance-<target>]
    user = <user>
    command = /srv/sites/bobvance/env/bin/uwsgi --socket 127.0.0.1:8001 --wsgi-file /srv/sites/bobvance/src/bobvance/wsgi/wsgi_<target>.py
    home = /srv/sites/bobvance/env
    master = true
    processes = 8
    harakiri = 600
    autostart = true
    autorestart = true
    stderr_logfile = /srv/sites/bobvance/log/uwsgi_err.log
    stdout_logfile = /srv/sites/bobvance/log/uwsgi_out.log
    stopsignal = QUIT

Nginx
-----

.. code::

    upstream django_bobvance_<target> {
      ip_hash;
      server 127.0.0.1:8001;
    }

    server {
      listen :80;
      server_name  my.domain.name;

      access_log /srv/sites/bobvance/log/nginx-access.log;
      error_log /srv/sites/bobvance/log/nginx-error.log;

      location /500.html {
        root /srv/sites/bobvance/src/bobvance/templates/;
      }
      error_page 500 502 503 504 /500.html;

      location /static/ {
        alias /srv/sites/bobvance/static/;
        expires 30d;
      }

      location /media/ {
        alias /srv/sites/bobvance/media/;
        expires 30d;
      }

      location / {
        uwsgi_pass django_bobvance_<target>;
      }
    }
