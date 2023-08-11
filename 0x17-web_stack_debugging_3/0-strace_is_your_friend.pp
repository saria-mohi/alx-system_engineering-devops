# to automate our solution using puppet
exec { 'sed inline txt replacement':
  command => 'sed -i "s/.phpp/.php/g" /var/www/html/wp-settings.php',
  path    => '/bin',
}
