#!/usr/bin/env bash
#Changes to our configuration file using Puppet

file { '/etc/ssh/ssh_config':
  ensure => present,
}

file_line { 'Turn off password auth':
  path  =>  '/etc/ssh/ssh_config',
  line  =>  'PasswordAuthentication no',
  match =>  '^#PasswordAuthentication',
}

file_line { 'Declare identify file':
  path  =>  '/etc/ssh/ssh_config',
  line  =>  'IdentifyFile ~/.ssh/school',
  match =>  '^#IdentifyFile',
}
