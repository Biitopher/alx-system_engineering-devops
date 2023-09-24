#!/usr/bin/env bash
#Changes to our configuration file using Puppet

file { '/etc/ssh/ssh_config':
  ensure => present
}

file_line { 'Turn off password auth':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => '    PasswordAuthentication no',
}
file_line { 'Declare identity file':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => '    IdentityFile ~/.ssh/school',
}
