#!/usr/bin/env bash
#Install an configure nginx with puppet

# Ensure Nginx package is installed
package { 'nginx':
  ensure => installed,
}

# Ensure Nginx service is running and enabled
service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => Package['nginx'],
}

# Configure Nginx to listen on port 80
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => "server {
    listen 80;
    root /var/www/html;
    location / {
        index index.html;
    }
    location /redirect_me {
        return 301 http://example.com/newpage;
    }
}\n",
  notify  => Service['nginx'],
}

# Create a simple HTML page with "Hello World!"
file { '/var/www/html/index.html':
  ensure  => file,
  content => "<html><body>Hello World!</body></html>\n",
  require => Package['nginx'],
}

# Remove the default Nginx default configuration
file { '/etc/nginx/sites-enabled/default':
  ensure => absent,
  notify => Service['nginx'],
}
