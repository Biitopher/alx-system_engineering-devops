#Puppet script
exec { 'set limit to 2000':
  path	  => '/usr/bin/env',
  command => 'sed -i s/15/2000/ /etc/default/nginx'
}

exec { 'reboot nginx':
  command => '/usr/bin/env service nginx restart'
}
