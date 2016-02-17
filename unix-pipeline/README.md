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
