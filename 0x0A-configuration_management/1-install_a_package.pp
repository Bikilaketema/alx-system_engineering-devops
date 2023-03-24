class { '::python':
  ensure => 'installed',
  dev    => true,
}

package { 'python3-pip':
  ensure => 'installed',
}

exec { 'install-flask':
  command => '/usr/bin/pip3 install flask==2.1.0',
  path    => ['/usr/bin'],
  unless  => '/usr/bin/pip3 freeze | /bin/grep flask==2.1.0',
  require => [Package['python3-pip'], Class['::python']],
}

