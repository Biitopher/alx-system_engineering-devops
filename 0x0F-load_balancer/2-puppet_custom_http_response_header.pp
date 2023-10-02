#!/usr/bin/env bash
#custom HTTP header with Puppet

class custom_http_response_header {
  package { 'nginx':
    ensure => installed,
  }

  service { 'nginx':
    ensure  => 'running',
    enable  => true,
    require => Package['nginx'],
  }

  file { '/etc/nginx/sites-available/custom-header':
    ensure  => present,
    content => "
server {
    listen 80 default_server;
    listen [::]:80 default_server;
    root /var/www/html;
    index index.html index.htm index.nginx-debian.html;
    server_name _;
    add_header X-Served-By $::hostname;
}
",
    require => Package['nginx'],
  }

  file { '/etc/nginx/sites-enabled/custom-header':
    ensure  => 'link',
    target  => '/etc/nginx/sites-available/custom-header',
    require => File['/etc/nginx/sites-available/custom-header'],
  }

  exec { 'reload_nginx':
    command     => '/usr/sbin/service nginx reload',
    refreshonly => true,
    subscribe   => [File['/etc/nginx/sites-available/custom-header'], File['/etc/nginx/sites-enabled/custom-header']],
  }
}
