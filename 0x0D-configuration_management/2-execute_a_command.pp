# kill a process
exec { 'kills_process':
  path    => '/usr/bin/:/bin/',
  command => 'pkill killmenow',
}
