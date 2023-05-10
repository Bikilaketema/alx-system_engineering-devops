# Puppet manifest to fix a 500 error in WordPress by replacing 'phpp' with 'php' in wp-settings.php file.

exec { 'fixed-phpp':
  command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
  path    => '/bin';
}
