file { '/var/www/html/wp-settings.php':
  ensure => 'file',
  replace => 'true',
  content => template('my_module/wp-settings.erb'),
}

class my_module {
  # Define a template with the contents of the wp-settings.php file, with the "phpp" string replaced with "php"
  file { '/etc/puppetlabs/code/environments/production/modules/my_module/templates/wp-settings.erb':
    ensure  => 'file',
    content => "# Contents of wp-settings.php file with 'phpp' replaced with 'php'\n<?php\n// ...\n",
    source  => 'puppet:///modules/my_module/wp-settings.erb',
  }

  # Restart Apache after the wp-settings.php file has been updated
  service { 'httpd':
    ensure     => 'running',
    enable     => 'true',
    subscribe  => File['/var/www/html/wp-settings.php'],
  }
}

include my_module
