# phpp to php
exec { 'fix file typo':
path    => [ '/usr/bin', '/bin', '/usr/sbin' ],
cwd     => '/var/www/html/wp-includes',
command => 'mv class-wp-locale.phpp class-wp-locale.php',
}
