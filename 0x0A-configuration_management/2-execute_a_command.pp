#Kill the process menow
exec { 'killmenow':
  command => 'pkill -f killmenow'
}

