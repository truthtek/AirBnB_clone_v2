#!/usr/bin/python3
"""a script to pack static content into a tarball
"""
file { '/data':
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

file { '/data/web_static':
  ensure => 'directory',
  owner  => 'root',
  group  => 'root',
}

file { '/data/web_static/releases':
  ensure => 'directory',
  owner  => 'root',
  group  => 'root',
}

file { '/data/web_static/shared':
  ensure => 'directory',
  owner  => 'root',
  group  => 'root',
}

file { '/data/web_static/releases/test':
  ensure => 'directory',
  owner  => 'root',
  group  => 'root',
}

file { '/data/web_static/releases/test/index.html':
  ensure  => 'present',
  content => '
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
',
  owner   => 'root',
  group   => 'root',
}

file { '/data/web_static/current':
  ensure => 'link',
  target => '/data/web_static/releases/test',
  owner  => 'root',
  group  => 'root',
}

exec { 'nginx_config':
  command => 'echo "location /hbnb_static { alias /data/web_static/current/; }" >> /etc/nginx/sites-available/default && service nginx restart',
  path    => ['/bin', '/usr/bin'],
  require => Package['nginx'],
}
