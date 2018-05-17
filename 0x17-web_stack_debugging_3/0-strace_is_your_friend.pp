# phpp to php
exec { '/var/www/html/wp-settings.php':  
path    => [ '/usr/bin', '/bin', '/usr/sbin' ],
cwd     => '/var/www/html/wp-includes',  
command => "sed -i 's/.phpp/.php/g' /var/www/html/wp-settings.php"
}