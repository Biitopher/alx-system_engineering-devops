# Puppet script
exec { 'set limit':
  command => "sed -i's/15/4096/' /etc/default/nginx",
  path    => '/usr/local/bin/:/bin/'
}

# Nginx restart
-> exec { 'reboot nginx':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
