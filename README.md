envRunner is a command wrapper that provides configuration through environment variables. These variables can be set from a multitude of sources.                                                                
Examples:
```

    envRunner  test.yml exec some_command params
    envRunner test.json exec some_command params
    envRunner http://test.com/test.yml exec some_command params
    envRunner http://test.com/test.json exec some_command params

```

Each of the above will read the configuration file and then merge the values inside of that with the environment of the subprocess.

```
Usage:
  envRunner (-h | --help) 
  envRunner <config> exec [COMMAND ...]                                                                                
Options:
  -h --help   Shows this screen.                                                                                       
  --version  
```
