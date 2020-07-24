# ![Tractor](https://github.com/bluecolor/tractor/blob/master/tractor.png) Tractor

Plugin based cross platform data transfer utility.

Tractor is extendable data transfer utility between various source and target systems.
It utilizes input/output/and solo plugins to move data between providers and consumers.

## Installation

`pip install tractor`

## Configuration

Tractor stores the data transfer definitions, which are called **mapping** in YAML file.
Here is an example of a configuration file.
```yml
mappings:
- Demo:
    input:
        plugin: Oracle
        host: 192.168.1.196
        username: tractor
        password: tractor
        service_name: orcl
        columns: "*"
        table: table_3
    output:
        plugin: Oracle
        host: 192.168.1.196
        username: tractor
        password: tractor
        table: table_5
        columns:
            - name: A
              type: number
            - name: B
              type: date
            - name: C
              type: varchar2(100)
        service_name: orcl
        truncate: True
- DemoCsv:
    input:
        plugin: Oracle
        host: 192.168.1.196
        username: tractor
        password: tractor
        service_name: orcl
        columns: "*"
        table: table_3
    output:
        plugin: Csv
        file: /home/ceyhun/projects/lab/tractor/play/table_1.csv
```

The configuration file location is controlled by the `TRACTOR_CONFIG_FILE` environment variable. It defaults to
`tractor.yml` in the current working directory.
For example in linux you can change the config file location with;
```sh
export TRACTOR_CONFIG_FILE=/path/to/config.yml
```

### Configuration file format
```yml
# the skeleton of config file is like this;
# mappings: { [
    # { mapping_name: { mapping_body } },
    # { mapping_name: { mapping_body } },
    # ...
# ] }

# "mappings" : root of the mapping definitions
# "mapping_name" : Unique name of mapping
# transfer definition is called "mapping"
# list of mapping definitions are kept under "mappings" key
mappings:
# each mapping have the mapping name as the key and an further config details as value.
- Mapiing Name:
    input:
      ...props
    output:
      ...props
```


# Usage
Running mappings:
```sh
tractor run <mapping name>
```

### Logging
Logging is controlled by `TRACTOR_LOG_LEVEL` environment variable.
[See log levels](https://docs.python.org/3/library/logging.html#logging-levels)

