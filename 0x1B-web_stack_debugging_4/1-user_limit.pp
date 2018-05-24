# path -> sed -i 's/original/new/g' -> file
exec { 'remove-limit':
  path     => 'usr/bin/:/bin/',
  command  => 'sed -i -e "s/holberton/#holberton/g" /etc/security/limits.conf',
  provider => 'shell',
  notify   => Exec['restart-nginx'],
}

exec { 'restart-nginx':
  command  => 'sudo service nginx restart',
  provider => 'shell',
  require  => Exec['remove-limit'],
}
