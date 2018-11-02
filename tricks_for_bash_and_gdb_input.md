#pwn
##some tircks
	**print ABCD**
	`$ echo -e '\x41\x42\x43\x44'`
	`$ printf '\x41\x42\x43\x44'`
	`$ python -c 'print "\x41\x42\x43\x44"'`
	`$ perl -e 'print "\x41\x42\x43\x44";'`
	**print 100 A**
	`$ python -c 'print "A"*100'`
	**When in bash-as an argument**
	`$ ./vulnerable `your_command_here``
	`$ ./vulnerable $(your_command_here)`
	**When in bash as an input** 
	`$ your_command_here | ./vulnerable`
	**and in bash we can write to file **
	`$ your_command_here > filename`
	**Use file as input**
	`$ ./vulnerable < filename`
	**gdb io**
	`$ r $(your_command_here)`
	**Use command as input**
	`$ r < <(your_command_here)`
	**Write command output to file**
	`$ r > filename`
	**Use file as input**
	`$ r < filename`
	
