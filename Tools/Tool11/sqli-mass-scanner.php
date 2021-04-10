<?php 

################################
# github.com/tcpwrapped	       #	
# By 01008004 (Tcpwrapped)     #
################################

error_reporting(0);
set_time_limit(0);

if (count($argv) == 1) {
	$banner = "\e[31m\e[1m

   _____  ____  _      _____   __  __           _____ _____    _____  _____          _   _ _   _ ______ _____  
  / ____|/ __ \| |    |_   _| |  \/  |   /\    / ____/ ____|  / ____|/ ____|   /\   | \ | | \ | |  ____|  __ \ 
 | (___ | |  | | |      | |   | \  / |  /  \  | (___| (___   | (___ | |       /  \  |  \| |  \| | |__  | |__) |
  \___ \| |  | | |      | |   | |\/| | / /\ \  \___ \\___ \   \___ \| |      / /\ \ | . ` | . ` |  __| |  _  / 
  ____) | |__| | |____ _| |_  | |  | |/ ____ \ ____) |___) |  ____) | |____ / ____ \| |\  | |\  | |____| | \ \ 
 |_____/ \___\_\______|_____| |_|  |_/_/    \_\_____/_____/  |_____/ \_____/_/    \_\_| \_|_| \_|______|_|  \_\
                                                                                                               
                                                                                                               


\tUsage: php {$argv[0]} -l list.txt
\tUsage: php {$argv[0]} -u http://www.site.com/index.php?id=2\n";

}
	print($banner);

function requestSQLi($url,$key='1') {
	    $ch = curl_init();
	    curl_setopt($ch, CURLOPT_URL, $url."%27");
	    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

	    curl_setopt($ch, CURLOPT_TIMEOUT, 5);

	    $c  = curl_exec($ch);

	    if (strstr($c,"SQL")||strstr($c,"mysql_error")||strstr($c,"PDO")||strstr($c,"SQLSTATE")) {
	    	return "\e[034m$key -> \e[035m".$url." \e[32mVULNERABLE\n\e[0m";
	    } else {
	    	return "\e[034m$key -> \e[035m".$url." \e[31mNOT VULNERABLE\n\e[0m";
	    }

	}

	if (count($argv) == 3) {
		switch ($argv[1]) {
			case '-l':
				$file = $argv[2];
				if (file_exists($file)) {
					echo "\e[31m\e[1m
	 ___       _   ___       _        _   _            __  __            
	/ __| __ _| | |_ _|_ _  (_)___ __| |_(_)___ _ _   |  \/  |__ _ ______
	\__ \/ _` | |  | || ' \ | / -_) _|  _| / _ \ ' \  | |\/| / _` (_-<_-<
	|___/\__, |_| |___|_||_|/ \___\__|\__|_\___/_||_| |_|  |_\__,_/__/__/
        	|_|           |__/                                           
 	 ___                            
	/ __| __ __ _ _ _  _ _  ___ _ _ 
	\__ \/ _/ _` | ' \| ' \/ -_) '_|
	|___/\__\__,_|_||_|_||_\___|_| 	   github.com/tcpwrapped\n\n\e[0m";

					$file = explode("\n", file_get_contents($file));
					foreach ($file as $key => $line) {
						echo requestSQLi($line,$key+1);
					}
				}

				break;
			case '-u':
				$url = $argv[2];
				echo "\e[31m\e[1m
	 ___       _   ___       _        _   _            __  __            
	/ __| __ _| | |_ _|_ _  (_)___ __| |_(_)___ _ _   |  \/  |__ _ ______
	\__ \/ _` | |  | || ' \ | / -_) _|  _| / _ \ ' \  | |\/| / _` (_-<_-<
	|___/\__, |_| |___|_||_|/ \___\__|\__|_\___/_||_| |_|  |_\__,_/__/__/
        	|_|           |__/                                           
 	 ___                            
	/ __| __ __ _ _ _  _ _  ___ _ _ 
	\__ \/ _/ _` | ' \| ' \/ -_) '_|
	|___/\__\__,_|_||_|_||_\___|_| 	   github.com/tcpwrapped\n\n\e[0m";
				echo requestSQLi($url);

				break;
			
			default:
				echo "\e[31m\e[1m
	 ___       _   ___       _        _   _            __  __            
	/ __| __ _| | |_ _|_ _  (_)___ __| |_(_)___ _ _   |  \/  |__ _ ______
	\__ \/ _` | |  | || ' \ | / -_) _|  _| / _ \ ' \  | |\/| / _` (_-<_-<
	|___/\__, |_| |___|_||_|/ \___\__|\__|_\___/_||_| |_|  |_\__,_/__/__/
        	|_|           |__/                                           
 	 ___                            
	/ __| __ __ _ _ _  _ _  ___ _ _ 
	\__ \/ _/ _` | ' \| ' \/ -_) '_|
	|___/\__\__,_|_||_|_||_\___|_| 	   github.com/tcpwrapped\n\n \e[0m

\tUsage: php {$argv[0]} -l list.txt
\tUsage: php {$argv[0]} -u http://www.site.com/index.php?id=2\n\n";
				break;
		}
	} 

?>
