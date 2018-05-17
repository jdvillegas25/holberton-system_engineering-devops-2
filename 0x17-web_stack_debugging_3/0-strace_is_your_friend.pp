# phpp to php
exec { 'fix file typo':  
path    => '/usr/bin:/bin',  
command => 'mv class-wp-locale.phpp class-wp-locale.php',
}
