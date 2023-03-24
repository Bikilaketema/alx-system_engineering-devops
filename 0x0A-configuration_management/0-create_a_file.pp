#Creates a file in /tmp/school with the ff parameters

file { '/tmp/school':
 ensure  => file,
 path    => '/tmp/school', 
 mode    => '0744',
 owner   => 'www-data',
 group   => 'www-data',
 content => 'I Love Puppet'
}
