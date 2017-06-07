curl -s http://10140.polopoly.ninja:8080/status?rawdata | grep TimeSinceLastHeartbeat | awk -F '(,|:|=)' '{ printf "%-20s: %s\n", $5, $11 }' | sort -nrk3













DEFINITIONS
       The following definitions are used throughout the rest of this document.
       blank  A space or tab.
       word   A sequence of characters considered as a single unit by the shell.  Also known as a token.
       name   A word consisting only of alphanumeric characters and underscores, and beginning with an alphabetic character or an underscore.  Also referred to as
              an identifier.
       metacharacter
              A character that, when unquoted, separates words.  One of the following:
              |  & ; ( ) < > space tab
       control operator
              A token that performs a control function.  It is one of the following symbols:
              || & && ; ;; ( ) | |& <newline>


RESERVED WORDS
       Reserved words are words that have a special meaning to the shell.  The following words are recognized as reserved when unquoted and either the first  word
       of a simple command (see SHELL GRAMMAR below) or the third word of a case or for command:

       ! case  coproc  do done elif else esac fi for function if in select then until while { } time [[ ]]




Grammar:

"A simple command is a sequence of optional variable assignments followed by blank-separated words and redirections,
and terminated by a control operator. The first word specifies the command to be executed, and is passed as argument
zero.  The remaining words are passed as arguments to the invoked command."

Return value = exit status




   Lists
          A list is a sequence of one or more pipelines separated by one of the operators ;, &, &&, or ||, and optionally terminated by one of ;, &, or <newline>.

       Of these list operators, && and || have equal precedence, followed by ; and &, which have equal precedence.

       A sequence of one or more newlines may appear in a list instead of a semicolon to delimit commands.


       If a command is terminated by the control operator &, the shell executes the command in the background in a subshell.  The shell does not wait for the com-
              mand  to  finish,  and the return status is 0.  Commands separated by a ; are executed sequentially; the shell waits for each command to terminate in turn.
                     The return status is the exit status of the last command executed.

       AND and OR lists are sequences of one of more pipelines separated by the && and || control operators, respectively.  AND and OR  lists  are  executed  with
              left associativity.  An AND list has the form

              command1 && command2

       command2 is executed if, and only if, command1 returns an exit status of zero.

       An OR list has the form

              command1 || command2

       command2  is executed if and only if command1 returns a non-zero exit status.  The return status of AND and OR lists is the exit status of the last command
              executed in the list.





3.2.4 Compound Commands "Shell programming constructs"

• Looping Constructs:           Shell commands for iterative action.
  - until, while, for
• Conditional Constructs:       Shell commands for conditional execution.
  - if, case, select, ((...)), [[ expr ]]
• Command Grouping:             Ways to group commands.
 - (), {}


if :; then echo 'lol'; echo 'lal' > apa2.log; echo 'lil'; fi > apa.log











signals?




exit code









The simple command construct is the base for all higher constructs. Everything you execute, from pipelines to functions, finally ends up in (many) simple commands. That's why Bash only has one method to expand and execute a simple command.





This step happens after the initial command line splitting.

The expansion of a simple command is done in four steps (interpreting the simple command from left to right):

The words the parser has marked as variable assignments and redirections are saved for later processing.
variable assignments precede the command name and have the form WORD=WORD
redirections can appear anywhere in the simple command
The rest of the words are expanded. If any words remain after expansion, the first word is taken to be the name of the command and the remaining words are the arguments.
Redirections are performed.
The text after the = in each variable assignment undergoes tilde expansion, parameter expansion, command substitution, arithmetic expansion, and quote removal before being assigned to the variable.











COMMAND:

simple command
compound command
function definition
(Bash) coproc definition























Built in commands:
 - alias, bind, builtin, caller, command, declare, echo, enable, help, local, mapfile, printf, read, readarray, source, type, typeset, ulimit, unalias











* KEEP IT VERY, VERY, SIMPLE!
  * Ge exempel på pipelines, och förklara dem i detalj (eller bygg upp dem i steg för att lösa ett problem?)


* Glossary
  
  |-------------------+----------------------------------------------------------------------------------------------|
  | Word              | Meaning                                                                                      |
  |-------------------+----------------------------------------------------------------------------------------------|
  | Terminal          | The end of a serial communication channel.                                                   |
  | Terminal Emulator | An application (e.g. Terminal.app) that emulates a hardware terminal.                        |
  | Shell             | Command line interpreter.                                                                    |
  | Standard Streams  | "stdin", "stdout", "stderr".  Sequences of bytes -- often ASCII text.                        |
  | Redirection       | Commanding the shell to redirect the standard streams (default: keyboard / terminal window). |
  | Pipe              | Connecting the output of one program to the input of another.                                |
  | Pipeline          | Two or more programs connected by pipes.                                                     |
  |-------------------+----------------------------------------------------------------------------------------------|


* Fundamentals
  * This is the Unix philosophy
    * Write programs that do one thing and do it well. Write programs to work together. Write programs to handle text streams, because that is a universal interface.
      1. Modularity
      2. Composition
      3. Minimalism
  * Standard streams
  * Stream redirection
  * Pipelines (parallel execution)
  * Unix filters
  * Composition
  * Shell?
  * Computation


* Example filters
  * cat
  * grep
  * sed
  * tr
  * sort
  * uniq
  * tee


* Interpreting a command
  * Enter line
  * Parse line
    * Split on command separators
    * Expansion
  * Redirections / Wiring up the pipeline
  * Executing
  * SIGPIPE


* Facts about command line parsing and executin
  1. "Bash is an sh-compatible command language interpreter that executes commands read from standard input or from a file."
  2. 


$ while number=$(curl -s http://10120.polopoly.ninja:8080/status?rawdata | grep application=image-service | grep -o TimeSinceLastHeartbeat:.* | cut -c 24-); do (( $number > 4000 )) && echo $number; don








import java.util.Scanner;
import java.util.regex.Pattern;

public class Grep {
    public static void main(String[] args) {
        Pattern pattern = Pattern.compile(args[0]);
        Scanner scanner = new Scanner(System.in);
        while (scanner.hasNextLine()) {
            String line = scanner.nextLine();
            if (pattern.matcher(line).find()) {
                System.out.println(line);
            }
        }
    }
}
