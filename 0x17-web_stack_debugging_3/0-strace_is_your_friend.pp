# Puppet manifest to fix a 500 error in WordPress by replacing 'phpp' with 'php' in wp-settings.php file.

# This manifest uses an 'exec' resource to run the 'sed' command with the specified options. 
# The 'command' parameter specifies the command to be executed, which replaces all occurrences of 'phpp' with 'php' in the wp-settings.php file. 
# The 'path' parameter specifies the location of the sed command.

exec { 'fixed-phpp':
  command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
  path    => '/bin';
}
