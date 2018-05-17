# path ->, sed -i 's/original/new/g' file.txt
exec { 'fix-phpp':
  path     => 'usr/bin/:/bin/',
  command  => "sed -i -e 's/.phpp/.php/g' /var/www/html/wp-settings.php",
  provider => 'shell',
}
