<h1><u>LL(1) Parser</u><br>
Compiler Design Project, Semester 5</h1><br>
<pre>
Implemented in -> Python 3
Extra python packages required :
    (a) PrettyTable
        Can be installed using - pip install PrettyTable

Objective -> To parse a given tokenised string according to given LL(1) grammar
             and check whether the string is valid or not.

Inputs to the program :
    1. A txt file for specifying the production rules of the grammar. It should
       follow the below format
       (a) All the productions of one variable must be on a single line separated by pipe symbol '|'
           e.g. A -> aAb | cD  is right
                A -> aAb
                A -> cD
                Specifying on two different lines is wrong
       (b) There must be exactly one space before and one space after the pipe symbol '|'
       (c) LHS and RHS must be separated by ->
           and there must be exactly one space before and one space after the arrow symbol '->'
       (d) Null is denoted by ^
       (e) Single uppercase letter is used for a non-terminal
       (f) Terminals may be composed of lowercase letters and special characters
       (g) See example grammar files for further clarification

    2. Another txt file for specifying the terminal symbols
       (a) One terminal per line
       (b) ^ should also be treated as a terminal. So if ^ is present in production rules then
           ^ must be written in this file. See grammar4.txt and terminal4.txt

    Which grammar and terminal file to take as input can be specified in final.py at line number 16 and 27
    respectively

    3. Another txt file for the input string to be parsed. See input.txt
       Which file to use can be changed at line 66 in final.py

Execute command - python3 final.py

Outputs of the program :
    1. First of all, first and follow of all variables are determined and displayed.
    2. Then if the grammar is LL(1), Parsing table is generated and displayed,
       otherwise program is aborted.
    3. Then step by step parsing is done using a stack. Standard parsing for top-down parser is done.
    4. Then final output is displayed whether string is ACCEPTED or REJECTED.


--> Submitted to - Dr. Dinesh Gopalani, Dept. of CSE, MNIT Jaipur
--> Submitted by - AYUSH JAIN         ( 2017UCP1168 )
                   PRANSHU KHANDELWAL ( 2017UCP1200 )
</pre>
