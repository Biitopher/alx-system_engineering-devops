#Using Puppet, create a manifest that kills a process

exec { 'killmenow':
  command => 'pkill -9 killmenow',
  onlyif  => 'pgrep killmenow',
  path    => '/usr/bin:/usr/sbin:/bin',
  logoutput => true,
}
