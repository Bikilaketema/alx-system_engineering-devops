#Kill the process menow
exec { 'kill-killmenow':
  command => 'pkill -f killmenow'
}

