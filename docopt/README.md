docopt.org
Ruby, Lua, Bash, C, JavaScript, etc...

Typical usage example:

Copy the usage printout of a similar command, add as docstring, parse __doc__...

Example:
- arguments
    -x 
    --ex
- options
    -x foo
    -xfoo
    --ex foo
    --ex=foo
- commands 
- optional
    [command --option <argument>]
    [command] [--option] [<argument>]
- required
    - Required by default
    - (--either-this <and-that> | <or-this>)
- mutually exclusive
    - foo | bar
- One or a group
    - element...
- End of options
    - --
- Default
    --ex Something
         [default value]

