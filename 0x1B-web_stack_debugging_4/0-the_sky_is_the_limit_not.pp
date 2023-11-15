#Puppet script
exec { 'set limit':
  path	  => '/usr/local/bin/:/bin/',
  command => "sed -i 's/15/4096/' /etc/default/nginx"
}

-> exec { 'reboot nginx':
   path    => '/etc/init.d/',
   command => 'service nginx restart'
}
