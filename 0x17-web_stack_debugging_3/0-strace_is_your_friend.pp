# phpp to php
exec { 'fix file typo':  
path    => '/usr/bin:/bin',  
command => 'mv class-wp-locale.php class-wp-locale.phpp',
}