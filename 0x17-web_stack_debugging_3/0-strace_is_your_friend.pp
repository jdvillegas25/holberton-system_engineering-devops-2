# path -> path used for command execution...
# sed -i 's/original/new/g' file.txt
exec { ‘just-work’:
  path => ‘usr/bin/:/bin/’,
  command => "sed -i 's/.phpp/.php/g' /var/www/html/wp-settings.php",
}
