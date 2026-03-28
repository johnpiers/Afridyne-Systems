---
icon: octicons/pulse-24
---

![Local image](./images/bash.png){: style="display: block; margin: 0 auto"}
<H1 style="text-align: center;">Bash Scripting Github</H1>

!!! abstract "The Bourne - Again Shell"

    ``` markdown title="Bash Scripting."


    - Category: CLI
    - tags: [Featured]
    - Keywords:
     - Variables:
        - Functions
        - Interpolation
        - Brace expansions
        - Loops
        - Conditional execution
        - Command substitution
    ```


<span style="font-size: 1.5em;">Getting Started</span>

<span style="font-size: 1em;">Introduction</span>

This is a quick reference to getting started with Bash scripting.

- [Learn bash in y minutes](https://learnxinyminutes.com/docs/bash/) _(learnxinyminutes.com)_
- [Bash Guide](http://mywiki.wooledge.org/BashGuide) _(mywiki.wooledge.org)_
- [Bash Hackers Wiki](https://web.archive.org/web/20230406205817/https://wiki.bash-hackers.org/) _(wiki.bash-hackers.org)_

<span style="font-size: 1.2em;">Example</span> 

```bash
#!/usr/bin/env bash

name="John"
echo "Hello $name!"
```

<span style="font-size: 1.2em;">Variables</span>

```bash
name="John"
echo $name  # see below
echo "$name"
echo "${name}!"
```

<span style="font-size: .96em;">Generally Quote Your Variables Unless They Contain Wildcards to Expand or Command Fragments.</span>

```bash
wildcard="*.txt"
options="iv"
cp -$options $wildcard /tmp
```

<span style="font-size: 1.2em;">String Quotes</span> 

```bash
name="John"
echo "Hi $name"  #=> Hi John
echo 'Hi $name'  #=> Hi $name
```

<span style="font-size: 1.2em;">Shell Execution</span> 

```bash
echo "I'm in $(pwd)"
echo "I'm in `pwd`"  # obsolescent
# Same
```

See [Command Substitution](https://web.archive.org/web/20230326081741/https://wiki.bash-hackers.org/syntax/expansion/cmdsubst)

<span style="font-size: 1.2em;">Conditional Execution</span> 

```bash
git commit && git push
git commit || echo "Commit failed"
```

<span style="font-size: 1.2em;">Functions</span> 

```bash
get_name() {
  echo "John"
}

echo "You are $(get_name)"
```

See: [Functions](https://github.com/bobbyiliev/introduction-to-bash-scripting/blob/main/ebook/en/content/012-bash-functions.md)

<span style="font-size: 1.2em;">Conditionals</span>

```bash
if [[ -z "$string" ]]; then
  echo "String is empty"
elif [[ -n "$string" ]]; then
  echo "String is not empty"
fi
```

See: [Conditionals](https://github.com/bobbyiliev/introduction-to-bash-scripting/blob/main/ebook/en/content/010-bash-conditionals.md)

<span style="font-size: 1.2em;">Strict Mode</span>

```bash
set -euo pipefail
IFS=$'\n\t'
```

See: [Unofficial Bash Strict Mode](http://redsymbol.net/articles/unofficial-bash-strict-mode/)

<span style="font-size: 1.2em;">Brace Expansion</span>

```bash
echo {A,B}.js
```

| Expression             | Description           |
| ---------------------- | --------------------- |
| `{A,B}`                | Same as `A B`         |
| `{A,B}.js`             | Same as `A.js B.js`   |
| `{1..5}`               | Same as `1 2 3 4 5`   |
| <code>&lcub;{1..3},{7..9}}</code> | Same as `1 2 3 7 8 9` |

See: [Brace Expansion](https://web.archive.org/web/20230207192110/https://wiki.bash-hackers.org/syntax/expansion/brace)

<span style="font-size: 1.7em;">Parameter Expansions</span>

<span style="font-size: 1.2em;">Basics</span>

```bash
name="John"
echo "${name}"
echo "${name/J/j}"    #=> "john" (substitution)
echo "${name:0:2}"    #=> "Jo" (slicing)
echo "${name::2}"     #=> "Jo" (slicing)
echo "${name::-1}"    #=> "Joh" (slicing)
echo "${name:(-1)}"   #=> "n" (slicing from right)
echo "${name:(-2):1}" #=> "h" (slicing from right)
echo "${food:-Cake}"  #=> $food or "Cake"
```

```bash
length=2
echo "${name:0:length}"  #=> "Jo"
```

See: [Parameter Expansion](https://web.archive.org/web/20230408142504/https://wiki.bash-hackers.org/syntax/pe)

```bash
str="/path/to/foo.cpp"
echo "${str%.cpp}"    # /path/to/foo
echo "${str%.cpp}.o"  # /path/to/foo.o
echo "${str%/*}"      # /path/to

echo "${str##*.}"     # cpp (extension)
echo "${str##*/}"     # foo.cpp (basepath)

echo "${str#*/}"      # path/to/foo.cpp
echo "${str##*/}"     # foo.cpp

echo "${str/foo/bar}" # /path/to/bar.cpp
```

```bash
str="Hello world"
echo "${str:6:5}"    # "world"
echo "${str: -5:5}"  # "world"
```

```bash
src="/path/to/foo.cpp"
base=${src##*/}   #=> "foo.cpp" (basepath)
dir=${src%$base}  #=> "/path/to/" (dirpath)
```

<span style="font-size: 1.2em;">Prefix Name Expansion</span>

```bash
prefix_a=one
prefix_b=two
echo ${!prefix_*}  # all variables names starting with `prefix_`
prefix_a prefix_b
```

<span style="font-size: 1.2em;">Indirection</span>

```bash
name=joe
pointer=name
echo ${!pointer}
joe
```

<span style="font-size: 1.2em;">Substitution</span>

| Code              | Description         |
| ----------------- | ------------------- |
| `${foo%suffix}`   | Remove suffix       |
| `${foo#prefix}`   | Remove prefix       |
| ---               | ---                 |
| `${foo%%suffix}`  | Remove long suffix  |
| `${foo/%suffix}`  | Remove long suffix  |
| `${foo##prefix}`  | Remove long prefix  |
| `${foo/#prefix}`  | Remove long prefix  |
| ---               | ---                 |
| `${foo/from/to}`  | Replace first match |
| `${foo//from/to}` | Replace all         |
| ---               | ---                 |
| `${foo/%from/to}` | Replace suffix      |
| `${foo/#from/to}` | Replace prefix      |

<span style="font-size: 1.2em;">Comments</span>

```bash
# Single line comment
```

```bash
: '
This is a
multi line
comment
'
```

<span style="font-size: 1.2em;">Substrings</span>

| Expression      | Description                    |
| --------------- | ------------------------------ |
| `${foo:0:3}`    | Substring _(position, length)_ |
| `${foo:(-3):3}` | Substring from the right       |

<span style="font-size: 1.2em;">Substitution</span>Length

| Expression | Description      |
| ---------- | ---------------- |
| `${#foo}`  | Length of `$foo` |

<span style="font-size: 1.2em;">Manipulation</span>

```bash
str="HELLO WORLD!"
echo "${str,}"   #=> "hELLO WORLD!" (lowercase 1st letter)
echo "${str,,}"  #=> "hello world!" (all lowercase)

str="hello world!"
echo "${str^}"   #=> "Hello world!" (uppercase 1st letter)
echo "${str^^}"  #=> "HELLO WORLD!" (all uppercase)
```

<span style="font-size: 1.2em;">Default Values</span>

| Expression        | Description                                              |
| ----------------- | -------------------------------------------------------- |
| `${foo:-val}`     | `$foo`, or `val` if unset (or null)                      |
| `${foo:=val}`     | Set `$foo` to `val` if unset (or null)                   |
| `${foo:+val}`     | `val` if `$foo` is set (and not null)                    |
| `${foo:?message}` | Show error message and exit if `$foo` is unset (or null) |

Omitting the `:` removes the (non)nullity checks, e.g. `${foo-val}` expands to `val` if unset otherwise `$foo`.

<span style="font-size: 1.5em;">Loops</span> 

<span style="font-size: 1.2em;">Basic For Loop</span>

```bash
for i in /etc/rc.*; do
  echo "$i"
done
```

<span style="font-size: 1.2em;">C-like For Loop</span>

```bash
for ((i = 0 ; i < 100 ; i++)); do
  echo "$i"
done
```

<span style="font-size: 1.2em;">Ranges</span>

```bash
for i in {1..5}; do
    echo "Welcome $i"
done
```

<span style="font-size: 1.2em;">With Step Size</span>

```bash
for i in {5..50..5}; do
    echo "Welcome $i"
done
```

<span style="font-size: 1.2em;">Reading Lines</span>

```bash
while read -r line; do
  echo "$line"
done <file.txt
```

<span style="font-size: 1.2em;">Forever</span>

```bash
while true; do
  ···
done
```

<span style="font-size: 1.5em;">Functions</span>

<span style="font-size: 1.2em;">Defining Functions</span>

```bash
myfunc() {
    echo "hello $1"
}
```

```bash
# Same as above (alternate syntax)
function myfunc {
    echo "hello $1"
}
```

```bash
myfunc "John"
```

<span style="font-size: 1.2em;">Returning Values</span>

```bash
myfunc() {
    local myresult='some value'
    echo "$myresult"
}
```

```bash
result=$(myfunc)
```

<span style="font-size: 1.2em;">Raising Errors</span>

```bash
myfunc() {
  return 1
}
```

```bash
if myfunc; then
  echo "success"
else
  echo "failure"
fi
```

<span style="font-size: 1.2em;">Arguments</span>

| Expression | Description                                    |
| ---------- | ---------------------------------------------- |
| `$#`       | Number of arguments                            |
| `$*`       | All positional arguments (as a single word)    |
| `$@`       | All positional arguments (as separate strings) |
| `$1`       | First argument                                 |
| `$_`       | Last argument of the previous command          |

**Note**: `$@` and `$*` must be quoted in order to perform as described.
Otherwise, they do exactly the same thing (arguments as separate strings).

See [Special Parameters](https://web.archive.org/web/20230318164746/https://wiki.bash-hackers.org/syntax/shellvars#special_parameters_and_shell_variables).

<span style="font-size: 1.5em;">Conditionals</span>

<span style="font-size: 1.2em;">Conditions</span>

Note that `[[` is actually a command/program that returns either `0` (true) or `1` (false). Any program that obeys the same logic (like all base utils, such as `grep(1)` or `ping(1)`) can be used as condition, see examples.

| Condition                | Description           |
| ------------------------ | --------------------- |
| `[[ -z STRING ]]`        | Empty string          |
| `[[ -n STRING ]]`        | Not empty string      |
| `[[ STRING == STRING ]]` | Equal                 |
| `[[ STRING != STRING ]]` | Not Equal             |
| ---                      | ---                   |
| `[[ NUM -eq NUM ]]`      | Equal                 |
| `[[ NUM -ne NUM ]]`      | Not equal             |
| `[[ NUM -lt NUM ]]`      | Less than             |
| `[[ NUM -le NUM ]]`      | Less than or equal    |
| `[[ NUM -gt NUM ]]`      | Greater than          |
| `[[ NUM -ge NUM ]]`      | Greater than or equal |
| ---                      | ---                   |
| `[[ STRING =~ STRING ]]` | Regexp                |
| ---                      | ---                   |
| `(( NUM < NUM ))`        | Numeric conditions    |

<span style="font-size: 1em;">More Conditions</span>

| Condition            | Description              |
| -------------------- | ------------------------ |
| `[[ -o noclobber ]]` | If OPTIONNAME is enabled |
| ---                  | ---                      |
| `[[ ! EXPR ]]`       | Not                      |
| `[[ X && Y ]]`       | And                      |
| `[[ X || Y ]]`       | Or                       |

### File conditions

| Condition               | Description             |
| ----------------------- | ----------------------- |
| `[[ -e FILE ]]`         | Exists                  |
| `[[ -r FILE ]]`         | Readable                |
| `[[ -h FILE ]]`         | Symlink                 |
| `[[ -d FILE ]]`         | Directory               |
| `[[ -w FILE ]]`         | Writable                |
| `[[ -s FILE ]]`         | Size is > 0 bytes       |
| `[[ -f FILE ]]`         | File                    |
| `[[ -x FILE ]]`         | Executable              |
| ---                     | ---                     |
| `[[ FILE1 -nt FILE2 ]]` | 1 is more recent than 2 |
| `[[ FILE1 -ot FILE2 ]]` | 2 is more recent than 1 |
| `[[ FILE1 -ef FILE2 ]]` | Same files              |

### Example

```bash
# String
if [[ -z "$string" ]]; then
  echo "String is empty"
elif [[ -n "$string" ]]; then
  echo "String is not empty"
else
  echo "This never happens"
fi
```

```bash
# Combinations
if [[ X && Y ]]; then
  ...
fi
```

```bash
# Equal
if [[ "$A" == "$B" ]]
```

```bash
# Regex
if [[ "A" =~ . ]]
```

```bash
if (( $a < $b )); then
   echo "$a is smaller than $b"
fi
```

```bash
if [[ -e "file.txt" ]]; then
  echo "file exists"
fi
```

## Arrays

### Defining arrays

```bash
Fruits=('Apple' 'Banana' 'Orange')
```

```bash
Fruits[0]="Apple"
Fruits[1]="Banana"
Fruits[2]="Orange"
```

### Working with arrays

```bash
echo "${Fruits[0]}"           # Element #0
echo "${Fruits[-1]}"          # Last element
echo "${Fruits[@]}"           # All elements, space-separated
echo "${#Fruits[@]}"          # Number of elements
echo "${#Fruits}"             # String length of the 1st element
echo "${#Fruits[3]}"          # String length of the Nth element
echo "${Fruits[@]:3:2}"       # Range (from position 3, length 2)
echo "${!Fruits[@]}"          # Keys of all elements, space-separated
```

### Operations

```bash
Fruits=("${Fruits[@]}" "Watermelon")    # Push
Fruits+=('Watermelon')                  # Also Push
Fruits=( "${Fruits[@]/Ap*/}" )          # Remove by regex match
unset Fruits[2]                         # Remove one item
Fruits=("${Fruits[@]}")                 # Duplicate
Fruits=("${Fruits[@]}" "${Veggies[@]}") # Concatenate
words=($(< datafile))                   # From file (split by IFS)
```

### Iteration

```bash
for i in "${arrayName[@]}"; do
  echo "$i"
done
```

## Dictionaries

### Defining

```bash
declare -A sounds
```

```bash
sounds[dog]="bark"
sounds[cow]="moo"
sounds[bird]="tweet"
sounds[wolf]="howl"
```

Declares `sound` as a Dictionary object (aka associative array).

### Working with dictionaries

```bash
echo "${sounds[dog]}" # Dog's sound
echo "${sounds[@]}"   # All values
echo "${!sounds[@]}"  # All keys
echo "${#sounds[@]}"  # Number of elements
unset sounds[dog]     # Delete dog
```

### Iteration

#### Iterate over values

```bash
for val in "${sounds[@]}"; do
  echo "$val"
done
```

#### Iterate over keys

```bash
for key in "${!sounds[@]}"; do
  echo "$key"
done
```

## Options

### Options

```bash
set -o noclobber  # Avoid overlay files (echo "hi" > foo)
set -o errexit    # Used to exit upon error, avoiding cascading errors
set -o pipefail   # Unveils hidden failures
set -o nounset    # Exposes unset variables
```

### Glob options

```bash
shopt -s nullglob    # Non-matching globs are removed  ('*.foo' => '')
shopt -s failglob    # Non-matching globs throw errors
shopt -s nocaseglob  # Case insensitive globs
shopt -s dotglob     # Wildcards match dotfiles ("*.sh" => ".foo.sh")
shopt -s globstar    # Allow ** for recursive matches ('lib/**/*.rb' => 'lib/a/b/c.rb')
```

Set `GLOBIGNORE` as a colon-separated list of patterns to be removed from glob
matches.

## History

### Commands

| Command               | Description                               |
| --------------------- | ----------------------------------------- |
| `history`             | Show history                              |
| `shopt -s histverify` | Don't execute expanded result immediately |

### Expansions

| Expression   | Description                                          |
| ------------ | ---------------------------------------------------- |
| `!$`         | Expand last parameter of most recent command         |
| `!*`         | Expand all parameters of most recent command         |
| `!-n`        | Expand `n`th most recent command                     |
| `!n`         | Expand `n`th command in history                      |
| `!<command>` | Expand most recent invocation of command `<command>` |

### Operations

| Code                 | Description                                                           |
| -------------------- | --------------------------------------------------------------------- |
| `!!`                 | Execute last command again                                            |
| `!!:s/<FROM>/<TO>/`  | Replace first occurrence of `<FROM>` to `<TO>` in most recent command |
| `!!:gs/<FROM>/<TO>/` | Replace all occurrences of `<FROM>` to `<TO>` in most recent command  |
| `!$:t`               | Expand only basename from last parameter of most recent command       |
| `!$:h`               | Expand only directory from last parameter of most recent command      |

`!!` and `!$` can be replaced with any valid expansion.

### Slices

| Code     | Description                                                                              |
| -------- | ---------------------------------------------------------------------------------------- |
| `!!:n`   | Expand only `n`th token from most recent command (command is `0`; first argument is `1`) |
| `!^`     | Expand first argument from most recent command                                           |
| `!$`     | Expand last token from most recent command                                               |
| `!!:n-m` | Expand range of tokens from most recent command                                          |
| `!!:n-$` | Expand `n`th token to last from most recent command                                      |

`!!` can be replaced with any valid expansion i.e. `!cat`, `!-2`, `!42`, etc.

## Miscellaneous

### Numeric calculations

```bash
$((a + 200))      # Add 200 to $a
```

```bash
$(($RANDOM%200))  # Random number 0..199
```

```bash
declare -i count  # Declare as type integer
count+=1          # Increment
```

### Subshells

```bash
(cd somedir; echo "I'm now in $PWD")
pwd # still in first directory
```

### Redirection

```bash
python hello.py > output.txt            # stdout to (file)
python hello.py >> output.txt           # stdout to (file), append
python hello.py 2> error.log            # stderr to (file)
python hello.py 2>&1                    # stderr to stdout
python hello.py 2>/dev/null             # stderr to (null)
python hello.py >output.txt 2>&1        # stdout and stderr to (file), equivalent to &>
python hello.py &>/dev/null             # stdout and stderr to (null)
echo "$0: warning: too many users" >&2  # print diagnostic message to stderr
```

```bash
python hello.py < foo.txt      # feed foo.txt to stdin for python
diff <(ls -r) <(ls)            # Compare two stdout without files
```

### Inspecting commands

```bash
command -V cd
#=> "cd is a function/alias/whatever"
```

### Trap errors

```bash
trap 'echo Error at about $LINENO' ERR
```

or

```bash
traperr() {
  echo "ERROR: ${BASH_SOURCE[1]} at about ${BASH_LINENO[0]}"
}

set -o errtrace
trap traperr ERR
```

### Case/switch

```bash
case "$1" in
  start | up)
    vagrant up
    ;;

  *)
    echo "Usage: $0 {start|stop|ssh}"
    ;;
esac
```

### Source relative

```bash
source "${0%/*}/../share/foo.sh"
```

### printf

```bash
printf "Hello %s, I'm %s" Sven Olga
#=> "Hello Sven, I'm Olga

printf "1 + 1 = %d" 2
#=> "1 + 1 = 2"

printf "This is how you print a float: %f" 2
#=> "This is how you print a float: 2.000000"

printf '%s\n' '#!/bin/bash' 'echo hello' >file
# format string is applied to each group of arguments
printf '%i+%i=%i\n' 1 2 3  4 5 9
```

### Transform strings

| Command option | Description                                         |
| -------------- | --------------------------------------------------- |
| `-c`           | Operations apply to characters not in the given set |
| `-d`           | Delete characters                                   |
| `-s`           | Replaces repeated characters with single occurrence |
| `-t`           | Truncates                                           |
| `[:upper:]`    | All upper case letters                              |
| `[:lower:]`    | All lower case letters                              |
| `[:digit:]`    | All digits                                          |
| `[:space:]`    | All whitespace                                      |
| `[:alpha:]`    | All letters                                         |
| `[:alnum:]`    | All letters and digits                              |

#### Example

```bash
echo "Welcome To Devhints" | tr '[:lower:]' '[:upper:]'
WELCOME TO DEVHINTS
```

### Directory of script

```bash
dir=${0%/*}
```

### Getting options

```bash
while [[ "$1" =~ ^- && ! "$1" == "--" ]]; do case $1 in
  -V | --version )
    echo "$version"
    exit
    ;;
  -s | --string )
    shift; string=$1
    ;;
  -f | --flag )
    flag=1
    ;;
esac; shift; done
if [[ "$1" == '--' ]]; then shift; fi
```

### Heredoc

```sh
cat <<END
hello world
END
```

Heredoc allows a section of your source code to be treated as a file. See [Bash Reference Manual](https://www.gnu.org/software/bash/manual/html_node/Redirections.html#Here-Documents).

### Herestring

```sh
tr '[:lower:]' '[:upper:]' <<< "Will be uppercased, even $variable"
```

Herestring allows a string to be treated as a standard input (stdin). See [Bash Reference Manual](https://www.gnu.org/software/bash/manual/html_node/Redirections.html#Here-Strings).

### Process substitution

```sh 
# loop on myfunc output lines
while read -r line; do
  echo "$line"
done < <(myfunc)

# compare content of two folders
diff <(ls "$dir1") <(ls "$dir2")
```

Process substitution allows the input (or output) of a command to be treated as a file. See [Bash Reference Manual](https://www.gnu.org/software/bash/manual/html_node/Process-Substitution.html).

### Reading input

```bash
echo -n "Proceed? [y/n]: "
read -r ans
echo "$ans"
```

The `-r` option disables a peculiar legacy behavior with backslashes.

```bash
read -n 1 ans    # Just one character
```

### Special variables

| Expression         | Description                            |
| ------------------ | -------------------------------------- |
| `$?`               | Exit status of last task               |
| `$!`               | PID of last background task            |
| `$$`               | PID of shell                           |
| `$0`               | Filename of the shell script           |
| `$_`               | Last argument of the previous command  |
| `${PIPESTATUS[n]}` | return value of piped commands (array) |

See [Special parameters](https://web.archive.org/web/20230318164746/https://wiki.bash-hackers.org/syntax/shellvars#special_parameters_and_shell_variables).

### Go to previous directory

```bash
pwd # /home/user/foo
cd bar/
pwd # /home/user/foo/bar
cd -
pwd # /home/user/foo
```

### Check for command's result

```bash
if ping -c 1 google.com; then
  echo "It appears you have a working internet connection"
fi
```

### Grep check

```bash
if grep -q 'foo' ~/.bash_history; then
  echo "You appear to have typed 'foo' in the past"
fi
```

## Also see

- [Bash-hackers wiki](https://web.archive.org/web/20230406205817/https://wiki.bash-hackers.org/) _(bash-hackers.org)_
- [Shell vars](https://web.archive.org/web/20230318164746/https://wiki.bash-hackers.org/syntax/shellvars) _(bash-hackers.org)_
- [Learn bash in y minutes](https://learnxinyminutes.com/docs/bash/) _(learnxinyminutes.com)_
- [Bash Guide](http://mywiki.wooledge.org/BashGuide) _(mywiki.wooledge.org)_
- [ShellCheck](https://www.shellcheck.net/) _(shellcheck.net)_

<style>
  .wikitable {
    border-collapse: collapse;
    width: 100%;
    border: 1px solid #ccc;
  }
  .wikitable th, .wikitable td {
    border: 1px solid #ccc;
    padding: 8px;
    text-align: left;
  }
  .wikitable th {
    background-color: #FFFFFF;
    font-weight: bold;
    color: #333333; /* Text color in light mode */
  }

  /* Dark mode styles */
  @media (prefers-color-scheme: dark) {
    .wikitable {
      border-color: #F0F0F0;
    }
    .wikitable th, .wikitable td {
      border-color: #D0D0D0;
    }
    .wikitable th {
      background-color: #006C3B;
      color: #e0e0e0; /* Light grey for heading text in dark mode */
    }
    .wikitable td {
      color: #008B72; /* Light grey for content in dark mode */
    }
    .wikitable td.note {
      color: #fff; /* White for "Note" column in dark mode */
    }
  }
</style>

<table class="wikitable">
<tbody><tr>
<th>Action</th>
<th>Command</th>
<th>Note</th></tr>
<tr>
<th colspan="3">Analyzing the system state</th></tr>
<tr>
<td class="action"><b>Show system status</b></td>
<td><code>systemctl status</code></td>
<td></td></tr>
<tr>
<td class="action"><b>List running</b> units</td>
<td><code>systemctl</code> or<br><code>systemctl list-units</code></td>
<td></td></tr>
<tr>
<td class="action"><b>List failed</b> units</td>
<td><code>systemctl --failed</code></td>
<td></td></tr>
<tr>
<td class="action"><b>List installed</b> unit files<sup>1</sup></td>
<td><code>systemctl list-unit-files</code></td>
<td></td></tr>
<tr>
<td class="action"><b>Show process status</b> for a PID</td>
<td><code>systemctl status <i>pid</i></code></td>
<td><a href="/title/Cgroups" title="Cgroups">cgroup slice</a>, memory and parent</td></tr>
<tr>
<th colspan="3">Checking the unit status</th></tr>
<tr>
<td class="action"><b>Show a manual page</b> associated with a unit</td>
<td><code>systemctl help <i>unit</i></code></td>
<td>as supported by the unit</td></tr>
<tr>
<td class="action"><b>Status</b> of a unit</td>
<td><code>systemctl status <i>unit</i></code></td>
<td>including whether it is running or not</td></tr>
<tr>
<td class="action"><b>Check</b> whether a unit is enabled</td>
<td><code>systemctl is-enabled <i>unit</i></code></td>
<td></td></tr>
<tr>
<th colspan="3">Starting, restarting, reloading a unit</th></tr>
<tr>
<td class="action"><b>Start</b> a unit immediately</td>
<td><code>systemctl start <i>unit</i></code> as root</td>
<td></td></tr>
<tr>
<td class="action"><b>Stop</b> a unit immediately</td>
<td><code>systemctl stop <i>unit</i></code> as root</td>
<td></td></tr>
<tr>
<td class="action"><b>Restart</b> a unit</td>
<td><code>systemctl restart <i>unit</i></code> as root</td>
<td></td></tr>
<tr>
<td class="action"><b>Reload</b> a unit and its configuration</td>
<td><code>systemctl reload <i>unit</i></code> as root</td>
<td></td></tr>
<tr>
<td class="action"><b>Reload systemd manager</b> configuration<sup>2</sup></td>
<td><code>systemctl daemon-reload</code> as root</td>
<td>scan for new or changed units</td></tr>
<tr>
<th colspan="3">Enabling a unit</th></tr>
<tr>
<td class="action"><b>Enable</b> a unit to start automatically at boot</td>
<td><code>systemctl enable <i>unit</i></code> as root</td>
<td></td></tr>
<tr>
<td class="action"><b>Enable</b> a unit to start automatically at boot and <b>start</b> it immediately</td>
<td><code>systemctl enable --now <i>unit</i></code> as root</td>
<td></td></tr>
<tr>
<td class="action"><b>Disable</b> a unit to no longer start at boot</td>
<td><code>systemctl disable <i>unit</i></code> as root</td>
<td></td></tr>
<tr>
<td class="action"><b>Reenable</b> a unit<sup>3</sup></td>
<td><code>systemctl reenable <i>unit</i></code> as root</td>
<td>i.e. disable and enable anew</td></tr>
<tr>
<th colspan="3">Masking a unit</th></tr>
<tr>
<td class="action"><b>Mask</b> a unit to make it impossible to start<sup>4</sup></td>
<td><code>systemctl mask <i>unit</i></code> as root</td>
<td></td></tr>
<tr>
<td class="action"><b>Unmask</b> a unit</td>
<td><code>systemctl unmask <i>unit</i></code> as root</td>
<td></td></tr></tbody></table>

Operators for Integer Comparison

| Operator | Description |
| --- | --- |
| `-eq` | equal |
| `-ne` | not equal |
| `-gt` | greater than |
| `-ge` | greater than or equal to |
| `-lt` | less than |
| `-le` | less than or equal to |

Operators for String Comparison

| Operator | Description |
| --- | --- |
| `==` | equal |
| `!=` | not equal |
| `>` | greater than |
| `<` | less than |
| `-n` | string is not null |
| `-z` | string is null |


### Redirections

But what if you'd want to save the results to a file? Bash has a redirect operator > that may be used to control where the output is delivered.

```bash
some_command > out.log            # Redirect stdout to out.log
some_command 2> err.log           # Redirect stderr to file err.log
some_command 2>&1                 # Redirect stderr to stdout
some_command 1>/dev/null 2>&1     # Silence both stdout and stderr
```
  
Complete summary:
  
| Syntax     | StdOut visibility | StdErr visibility | StdOut in file | StdErr in file | existing file |
| --------   | ----------------- | ----------------- | -------------- | -------------- | ------------- |
| `>`          |   no              |   yes             |   yes          |   no           |  overwrite    |
| `>>`         |   no              |   yes             |   yes          |   no           |  append       |
| `2>`         |   yes             |   no              |   no           |   yes          |  overwrite    |
| `2>>`        |   yes             |   no              |   no           |   yes          |  append       |
| `&>`         |   no              |   no              |   yes          |   yes          |  overwrite    | 
| `&>>`        |   no              |   no              |   yes          |   yes          |  append       | 
| `tee`        |   yes             |   yes             |   yes          |   no           |  overwrite    |
| `tee -a`     |   yes             |   yes             |   yes          |   no           |  append       |
| `n.e. (*)`   |   yes             |   yes             |   no           |   yes          |  overwrite    | 
| `n.e. (*)`   |   yes             |   yes             |   no           |   yes          |  append       |
| `\|& tee`    |   yes             |   yes             |   yes          |   yes          |  overwrite    |
| `\|& tee -a` |   yes             |   yes             |   yes          |   yes          |  append       |


### Formatting and linting

It is important to keep the formatting of your script as consistent as possible. <a href="https://github.com/lovesegfault/beautysh">Beautysh</a> is an amazing tool that helps you to format your script. To use it, just run the following command in a directory where your scripts are located:

```bash
beautysh **/*.sh
```
  
Additionally we advise to use <a href="https://github.com/koalaman/shellcheck">shellcheck</a> for code inspection.

```bash
shellcheck **/*.sh
```

## Available scripts
 
### Intro

| # | Description                                                         | Code                                                                                     |
|---|---------------------------------------------------------------------|------------------------------------------------------------------------------------------|
| 1 | Prints "Hello, world!" to the console.                              | [hello_world.sh](https://github.com/djeada/Bash-scripts/blob/master/src/hello_world.sh) |
| 2 | Demonstrates the use of if statements to check conditions.          | [conditionals.sh](https://github.com/djeada/Bash-scripts/blob/master/src/conditionals.sh) |
| 3 | Shows the use of a while loop to repeatedly execute code.            | [while_loop.sh](https://github.com/djeada/Bash-scripts/blob/master/src/while_loop.sh) |
| 4 | Demonstrates the use of a for loop to iterate over elements.         | [for_loop.sh](https://github.com/djeada/Bash-scripts/blob/master/src/for_loop.sh) |
| 5 | Displays the digits of a given number, one digit per line.           | [digits.sh](https://github.com/djeada/Bash-Scripts/blob/master/src/digits.sh) |
| 6 | Prints all of the numbers within a specified range, one number per line. | [numbers_in_interval.sh](https://github.com/djeada/Bash-Scripts/blob/master/src/numbers_in_interval.sh) |
| 7 | Prints a Christmas tree pattern to the console.                       | [christmas_tree.sh](https://github.com/djeada/Bash-Scripts/blob/master/src/christmas_tree.sh) |
| 8 | Prompts the user for a response to a given question and stores their response in a variable. | [prompt_for_answer.sh](https://github.com/djeada/Bash-Scripts/blob/master/src/prompt_for_answer.sh) |

### Math

| # | Description                                                                                                      | Code                                                                                                |
|---|------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| 1 | Performs basic arithmetic operations (addition, subtraction, multiplication, and division) on two numbers.      | [arithmetic_operations.sh](https://github.com/djeada/Bash-scripts/blob/master/src/arithmetic_operations.sh) |
| 2 | Calculates the sum of all the arguments passed to it, treating them as numbers.                                  | [sum_args.sh](https://github.com/djeada/Bash-scripts/blob/master/src/sum_args.sh)                     |
| 3 | Converts a number from the decimal (base 10) system to its equivalent in the binary (base 2) system.             | [decimal_binary.sh](https://github.com/djeada/Bash-scripts/blob/master/src/decimal_binary.sh)           |
| 4 | Calculates the factorial of a given integer.                                                                    | [factorial.sh](https://github.com/djeada/Bash-scripts/blob/master/src/factorial.sh)                     |
| 5 | Determines whether a given number is a prime number or not.                                                     | [is_prime.sh](https://github.com/djeada/Bash-scripts/blob/master/src/is_prime.sh)                       |
| 6 | Calculates the square root of a given number.                                                                   | [sqrt.sh](https://github.com/djeada/Bash-scripts/blob/master/src/sqrt.sh)


### Strings

| # | Description                                                                                                                 | Code                                                                                               |
|---|---------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| 1 | Counts the number of times a specific character appears in a given string.                                                      | [count_char.sh](https://github.com/djeada/Bash-Scripts/blob/master/src/count_char.sh)             |
| 2 | Converts all uppercase letters in a given string to lowercase.                                                                  | [lower.sh](https://github.com/djeada/Bash-Scripts/blob/master/src/lower.sh)                       |
| 3 | Converts all lowercase letters in a given string to uppercase.                                                                  | [upper.sh](https://github.com/djeada/Bash-Scripts/blob/master/src/upper.sh)                       |
| 4 | Checks if a given string is a palindrome, i.e., a word that is spelled the same way forwards and backwards.                   | [is_palindrome.sh](https://github.com/djeada/Bash-Scripts/blob/master/src/is_palindrome.sh)      |
| 5 | Checks if two given strings are anagrams, i.e., if they are made up of the same letters rearranged in a different order.       | [are_anagrams.sh](https://github.com/djeada/Bash-Scripts/blob/master/src/are_anagrams.sh)        |
| 6 | Calculates the Hamming Distance between two strings, i.e., the number of positions at which the corresponding characters are different. | [hamming_distance.sh](https://github.com/djeada/Bash-Scripts/blob/master/src/hamming_distance.sh) |
| 7 | Sorts a given string alphabetically, considering all letters to be lowercase.                                                  | [sort_string.sh](https://github.com/djeada/Bash-Scripts/blob/master/src/sort_string.sh)          |
| 8 | Creates a word histogram.                                                  | [word_histogram.sh](https://github.com/djeada/Bash-Scripts/blob/master/src/word_histogram.sh)    |


### Arrays

| # | Description                                                                                                  | Code                                                                                                   |
|---|--------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| 1 | Calculates the arithmetic mean of a given list of numbers.                                                    | [arith_mean.sh](https://github.com/djeada/Bash-Scripts/blob/master/src/arith_mean.sh)                   |
| 2 | Finds the maximum value in a given array of numbers.                                                         | [max_array.sh](https://github.com/djeada/Bash-Scripts/blob/master/src/max_array.sh)                     |
| 3 | Finds the minimum value in a given array of numbers.                                                         | [min_array.sh](https://github.com/djeada/Bash-Scripts/blob/master/src/min_array.sh)                     |
| 4 | Removes duplicates from a given array of numbers.                                                            | [remove_duplicates_in_array.sh](https://github.com/djeada/Bash-Scripts/blob/master/src/remove_duplicates_in_array.sh) |

### Files

| #  | Description                                                                                    | Code                                                                                                           |
|----|------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| 1  | Counts the number of files in a specified directory.                                            | [count_files.sh](https://github.com/djeada/Bash-scripts/blob/master/src/count_files.sh)                       |
| 2  | Creates a new directory with a specified name.                                                 | [make_dir.sh](https://github.com/djeada/Bash-scripts/blob/master/src/make_dir.sh)                             |
| 3  | Counts the number of lines in a specified text file.                                           | [line_counter.sh](https://github.com/djeada/Bash-scripts/blob/master/src/line_counter.sh)                     |
| 4  | Gets the middle line from a specified text file.                                               | [middle_line.sh](https://github.com/djeada/Bash-scripts/blob/master/src/middle_line.sh)                       |
| 5  | Removes duplicate lines from a specified file.                                                 | [remove_duplicate_lines.sh](https://github.com/djeada/Bash-Scripts/blob/master/src/remove_duplicate_lines.sh) |
| 6  | Replaces all forward slashes with backward slashes and vice versa in a specified file.        | [switch_slashes.sh](https://github.com/djeada/Bash-Scripts/blob/master/src/switch_slashes.sh)                 |
| 7  | Adds specified text to the beginning of a specified file.                                      | [prepend_text_to_file.sh](https://github.com/djeada/Bash-Scripts/blob/master/src/prepend_text_to_file.sh)     |
| 8  | Removes all lines in a specified file that contain only whitespaces.                           | [remove_empty_lines.sh](https://github.com/djeada/Bash-Scripts/blob/master/src/remove_empty_lines.sh)         |
| 9  | Renames all files in a specified directory with a particular extension to a new extension.    | [rename_extension.sh](https://github.com/djeada/Bash-Scripts/blob/master/src/rename_extension.sh)             |
| 10 | Strips digits from every string found in a given file.                                          | [strip_digits.sh](https://github.com/djeada/Bash-Scripts/blob/master/src/strip_digits.sh)                     |
| 11 | Lists the most recently modified files in a given directory.                                   | [recently_modified_files.sh](https://github.com/djeada/Bash-Scripts/blob/master/src/recently_modified_files.sh) |


### System administration

| #  | Description                                                                                                                           | Code                                                                                                             |
|----|---------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|
| 1  | Retrieves basic system information, such as hostname and kernel version.                                                             | [system_info.sh](https://github.com/djeada/Bash-scripts/blob/master/src/system_info.sh)                         |
| 2  | Determines the type and version of the operating system running on the machine.                                                      | [check_os.sh](https://github.com/djeada/Bash-scripts/blob/master/src/check_os.sh)                               |
| 3  | Checks whether the current user has root privileges.                                                                                  | [check_if_root.sh](https://github.com/djeada/Bash-Scripts/blob/master/src/check_if_root.sh)                     |
| 4  | Checks if the apt command, used for package management on Debian-based systems, is available on the machine.                          | [check_apt_avail.sh](https://github.com/djeada/Bash-Scripts/blob/master/src/check_apt_avail.sh)                 |
| 5  | Retrieves the size of the machine's random access memory (RAM).                                                                       | [ram_memory.sh](https://github.com/djeada/Bash-Scripts/blob/master/src/ram_memory.sh)                           |
| 6  | Gets the current temperature of the machine's central processing unit (CPU).                                                          | [cpu_temp.sh](https://github.com/djeada/Bash-scripts/blob/master/src/cpu_temp.sh)                               |
| 7  | Retrieves the current overall CPU usage of the machine.                                                                               | [cpu_usage.sh](https://github.com/djeada/Bash-Scripts/blob/master/src/cpu_usage.sh)                             |
| 8  | Blocks certain websites from being visited on the local machine by modifying the hosts file.                                          | [web_block.sh](https://github.com/djeada/Bash-Scripts/blob/master/src/web_block.sh)                             |
| 9  | Creates a backup of the system's files, compresses the backup, and encrypts the resulting archive for storage.                      | [backup.sh](https://github.com/djeada/Bash-scripts/blob/master/src/backup.sh)                                   |
| 10 | Displays processes that are not being waited on by any parent process. Orphan processes are created when the parent process terminates. | [orphans.sh](https://github.com/djeada/Bash-scripts/blob/master/src/orphans.sh)                                 |
| 11 | Displays processes that are in an undead state, also known as a "zombie" state. Zombie processes have completed execution but remain in the process table.   | [zombies.sh](https://github.com/djeada/Bash-scripts/blob/master/src/zombies.sh)                                 |

### Programming workflow

| # | Description                                                                                                                                                                                                                    | Code                                                                                                           |
|---|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| 1 | Removes the carriage return character (`\r`) from the given files, which may be present in files transferred between systems with different line ending conventions.                                                            | [remove_carriage_return.sh](https://github.com/djeada/Bash-scripts/blob/master/src/remove_carriage_return.sh) |
| 2 | Replaces all characters with diacritical marks in the given files with their non-diacritical counterparts. Diacritical marks are small signs added above or below letters to indicate different pronunciations or tones in some languages. | [remove_diacritics.sh](https://github.com/djeada/Bash-scripts/blob/master/src/remove_diacritics.sh)         |
| 3 | Changes all spaces in file names to underscores and converts them to lowercase. This can be useful for making the file names more compatible with systems that do not support spaces in file names or for making the file names easier to read or type. | [correct_file_names.sh](https://github.com/djeada/Bash-scripts/blob/master/src/correct_file_names.sh)       |
| 4 | Removes any trailing whitespace characters (spaces or tabs) from the end of every file in a given directory. Trailing whitespace can cause formatting issues or interfere with certain tools and processes.                             | [remove_trailing_whitespaces.sh](https://github.com/djeada/Bash-Scripts/blob/master/src/remove_trailing_whitespaces.sh) |
| 5 | Formats and beautifies every shell script found in the current repository. This can make the scripts easier to read and maintain by adding consistent indentation and whitespace.                                                         | [beautify_script.sh](https://github.com/djeada/Bash-Scripts/blob/master/src/beautify_script.sh)             |
| 6 | Finds functions and classes in a Python project that are not being used or called anywhere in the code. This can help identify and remove unnecessary code, which can improve the project's performance and maintainability.           | [dead_code.sh](https://github.com/djeada/Bash-Scripts/blob/master/src/dead_code.sh)                         |

### Git

| # | Description                                                                                                                                                                                                                                                                                                 | Code                                                                                                                      |
|---|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| 1 | Resets the local repository to match the state of the remote repository, discarding any local commits and changes. This can be useful for starting over or synchronizing with the latest version on the remote repository.                                                                                           | [reset_to_origin.sh](https://github.com/djeada/Bash-scripts/blob/master/src/reset_to_origin.sh)                                        |
| 2 | Deletes the specified branch both locally and on the remote repository. This can be useful for removing branches that are no longer needed or for consolidating multiple branches into a single branch.                                                                                                            | [remove_branch.sh](https://github.com/djeada/Bash-scripts/blob/master/src/remove_branch.sh)                                         |
| 3 | Counts the total number of lines of code in a git repository, including lines in all branches and commits. This can be useful for tracking the size and complexity of a project over time.                                                                                                                  | [count_lines_of_code.sh](https://github.com/djeada/Bash-scripts/blob/master/src/count_lines_of_code.sh)                                    |
| 4 | Combines multiple commits into a single commit. This can be useful for simplifying a commit history or for cleaning up a series of small, incremental commits that were made in error.                                                                                                                       | [squash_n_last_commits.sh](https://github.com/djeada/Bash-Scripts/blob/master/src/squash_n_last_commits.sh)                                 |
| 5 | Removes the `n` last commits from the repository. This can be useful for undoing mistakes or for removing sensitive information that was accidentally committed.                                                                                                                                              | [remove_n_last_commits.sh](https://github.com/djeada/Bash-Scripts/blob/master/src/remove_n_last_commits.sh)                                  |
| 6 | Changes the date of the last commit in the repository. This can be useful for altering the commit history for cosmetic purposes.                                                                                                                                                                            | [change_commit_date.sh](https://github.com/djeada/Bash-Scripts/blob/master/src/change_commit_date.sh)                                   |
| 7 | Downloads all of the public repositories belonging to a specified user on GitHub. This can be useful for backing up repositories.                                                                                                                                                                              | [download_all_github_repos.sh](https://github.com/djeada/Bash-Scripts/blob/master/src/download_all_github_repos.sh)                            |
| 8 | Squashes all commits on a specified Git branch into a single commit.                                                                                                                                                                              | [squash_branch.sh](https://github.com/djeada/Bash-Scripts/blob/master/src/squash_branch.sh)                            |
| 9 | Counts the total lines changed by a specific author in a Git repository.                                                                                                                                                                               | [contributions_by_git_author.sh](https://github.com/djeada/Bash-Scripts/blob/master/src/contributions_by_git_author.sh)                            |
  
### Utility

| # | Description | Code |
|---|-------------|------|
| 1	| Finds the public IP address of the device running the script. | [ip_info.sh](https://github.com/djeada/Bash-scripts/blob/master/src/ip_info.sh) |
| 2	| Deletes all files in the trash bin. | [empty_trash.sh](https://github.com/djeada/Bash-scripts/blob/master/src/empty_trash.sh) |
| 3	| Extracts files with a specified extension from a given directory. | [extract.sh](https://github.com/djeada/Bash-Scripts/blob/master/src/extract.sh) |
| 4	| Determines which programs are currently using a specified port number on the local system. | [program_on_port.sh](https://github.com/djeada/Bash-Scripts/blob/master/src/program_on_port.sh) |
| 5	| Converts month names to numbers and vice versa in a string. For example, "January" to "1" and "1" to "January". | [month_to_number.sh](https://github.com/djeada/Bash-Scripts/blob/master/src/month_to_number.sh) |
| 6	| Creates command aliases for all the scripts in a specified directory, allowing them to be run by simply typing their names. | [alias_all_the_scripts.sh](https://github.com/djeada/Bash-scripts/blob/master/src/alias_all_the_scripts.sh) |
| 7	| Generates a random integer within a given range. The range can be specified as arguments to the script. | [rand_int.sh](https://github.com/djeada/Bash-Scripts/blob/master/src/rand_int.sh) |
| 8	| Generates a random password of the specified length, using a combination of letters, numbers, and special characters. | [random_password.sh](https://github.com/djeada/Bash-Scripts/blob/master/src/random_password.sh) |
| 9	| Measures the time it takes to run a program with the specified input parameters. Output the elapsed time in seconds. | [time_execution.sh](https://github.com/djeada/Bash-scripts/blob/master/src/time_execution.sh) |
| 10	| Downloads the audio from a YouTube video or playlist in MP3 format. Specify the video or playlist URL and the destination directory for the downloaded files. | [youtube_to_mp3.sh](https://github.com/djeada/Bash-scripts/blob/master/src/youtube_to_mp3.sh) |
| 11	| Clears the local caches in the user's cache directory (e.g. `~/.cache`) that are older than a specified number of days. | [clear_cache.sh](https://github.com/djeada/Bash-scripts/blob/master/src/clear_cache.sh) |
| 12 | Resizes all JPG files in the current directory to a specified dimension (A4). | [resize_to_a4](https://github.com/djeada/Bash-Scripts/edit/master/src/resize_to_a4.sh) |

## References

### Official Documentation
- [GNU Bash Manual](https://www.gnu.org/software/bash/manual/bash.html): The official documentation for GNU Bash, detailing built-in commands, syntax, and features.
- [Linux Documentation Project](https://www.tldp.org/): Comprehensive collection of HOWTOs, guides, and FAQs for Linux users and administrators.

### Guides and Tutorials
- [Bash Guide by Greg's Wiki](http://mywiki.wooledge.org/BashGuide): An excellent resource for learning Bash scripting, written in an approachable and detailed manner.
- [Advanced Bash-Scripting Guide](https://tldp.org/LDP/abs/html/): A thorough guide for mastering advanced Bash scripting techniques and best practices.
- [Bash Hackers Wiki](https://wiki.bash-hackers.org/): In-depth explanations and tips for Bash scripting, focusing on practical usage and pitfalls.

### Learning Platforms
- [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line): An interactive platform for beginners to learn basic command line skills.
- [edX's Linux Foundation Courses](https://www.edx.org/school/linuxfoundationx): Online courses covering various aspects of Linux, including command line proficiency and system administration.

### Community and Support
- [Unix & Linux Stack Exchange](https://unix.stackexchange.com/): A Q&A site for users of Linux, FreeBSD, and other Un*x-like operating systems.
- [Reddit's r/bash](https://www.reddit.com/r/bash/): A subreddit dedicated to discussions and questions about Bash scripting and shell programming.

### Tools and Utilities
- [ShellCheck](https://www.shellcheck.net/): An online tool that helps you find and fix bugs in your shell scripts.
- [Explainshell](https://explainshell.com/): A web application that breaks down complex command lines into simple explanations.
- [Oh My Zsh](https://ohmyz.sh/): A framework for managing your Zsh configuration, making it easier to customize your shell.

### Books
- "Learning the bash Shell" by Cameron Newham: A comprehensive guide to Bash programming, suitable for beginners and experienced users alike.
- "Linux Command Line and Shell Scripting Bible" by Richard Blum and Christine Bresnahan: A detailed book covering Linux command line and shell scripting from the basics to advanced topics.
- "Bash Cookbook" by Carl Albing, JP Vossen, and Cameron Newham: A collection of useful Bash scripting recipes for various tasks and problems.

### Blogs and Articles
- [Linux Journal's Bash Articles](https://www.linuxjournal.com/tag/bash): A series of articles covering various Bash scripting topics and tips.
- [DigitalOcean's Bash Tutorials](https://www.digitalocean.com/community/tutorial_series/understanding-bash): Tutorials and guides to help you understand and use Bash effectively.
- [Bash-One-Liners Explained](https://www.bashoneliners.com/): A collection of Bash one-liners, with explanations on how they work and when to use them.



