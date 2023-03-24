#Creates a file in /tmp/school with the ff parameters
file { '/tmp/school':
 path    => '/tmp/school', 
 ensure  => file,
 content => 'I Love Puppet',
 mode    => '0744',
 owner   => 'www-data',
 group   => 'www-data',
}
