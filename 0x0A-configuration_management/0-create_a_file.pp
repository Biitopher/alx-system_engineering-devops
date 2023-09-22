#Creates file using Puppet
file { '/tmp/school':
  ensure  => file,            # Ensure it's a file
  mode    => '0744',          # File permissions
  owner   => 'www-data',     # File owner
  group   => 'www-data',     # File group
  content => 'I love Puppet', # File content
}
