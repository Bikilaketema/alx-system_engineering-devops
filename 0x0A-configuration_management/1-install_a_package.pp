class { '::python':
  ensure => 'installed',
  dev    => true,
}

package { 'python3-pip':
  ensure => 'installed',
}

exec { 'install-flask':
  path    => ['/usr/bin'],
  command => 'pip3 install flask==2.1.0',
  unless  => '/usr/bin/pip3 freeze | /bin/grep -w flask==2.1.0',
  require => [Package['python3-pip'], Class['::python']],
}
