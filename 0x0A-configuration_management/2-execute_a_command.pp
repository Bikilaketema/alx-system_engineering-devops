#Kill the process menow
exec { 'killmenow':
  command     => 'pkill -f killmenow',
  path        => ['/bin', '/usr/bin'],
  onlyif      => 'pgrep -f killmenow',
  logoutput   => true,
  refreshonly => true,
}

