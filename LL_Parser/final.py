import re
from prettytable import PrettyTable
from First import first_fn
from Follow import follow_fn
from ParsingTable import parsing_table
import Stack as st

def input_string_printer(input_list,input_pointer):
	str = ''
	for i in input_list[input_pointer:]:
		str = str + i + " "
	return str

if __name__ == '__main__':
	production = dict()     # Productions for each variable as a dictionary with key as variable
	fhandle = open("grammar1.txt","r")   # file containing production rules
	flag = 1
	for line in fhandle:
		line = line.rstrip()
		tmp_list = re.split(" -> | \| ", line)
		lhs = str(tmp_list[0])
		rhs = tmp_list[1:]
		if flag:
			start_symbol = lhs
			flag = 0
		production[lhs] = rhs
	terminal_file = open('terminal1.txt','r')         # file containing terminal symbols
	terminal = []                                     # list of terminal symbols
	for each in terminal_file:
		each = each.rstrip()
		terminal.append(each)

	print('\nTerminal Symbols =',terminal)
	#print(production)
	first_of_variables = first_fn(production,terminal)
	follow_of_variables = follow_fn(production,terminal,start_symbol,first_of_variables)
	###############################################################
	print('\nFirst of Variables : ')
	for var in first_of_variables:
		print(var,'-',first_of_variables[var])
	print('\nFollow of Variables : ')
	for var in follow_of_variables:
		print(var,'-',follow_of_variables[var])
	###############################################################
	table = parsing_table(production,terminal,first_of_variables,follow_of_variables)
	#print(table)
	print('\nParsing Table')
	########### TABLE FORMATTING #############
	tmp_table = table
	x = terminal
	if '^' in x:
		x.remove('^')
	x.append('$') ; x.sort()
	l1 = ['Var/Term']
	x = ['Var/Term'] + x
	obj = PrettyTable(x)
	for var in tmp_table:
		tmp_list = list(var)
		ddd = tmp_table[var]
		for key in sorted(ddd):
			tmp_list.append(ddd[key])
		obj.add_row(tmp_list)
	print(obj)
	##########################################
	######### PARSING OF INPUT STRING ########
	input_file = open("input.txt","r");
	for line in input_file:
		input_string = line.rstrip()

	input_string = input_string + '$'
	#print(input_string)
	input_list = []

	tmp_input_string = ''
	#print(terminal)
	for i in input_string:
		if i != ' ':
			tmp_input_string = tmp_input_string + i
		#print(tmp_input_string)
		if tmp_input_string in terminal:
			input_list.append(tmp_input_string)
			tmp_input_string = ''
	#input_list.append('$')
	print()
	print(input_list,'\n')
    ################# STACK #####################
	valid = 1
	input_pointer = 0
	stack = st.Stack()
	stack.push('$')
	stack.push(start_symbol)
	print(stack.print_bottom_up() + "		" + input_string_printer(input_list,input_pointer))

	while stack.top() != '$':
		top_sym = stack.top()
		next_input = input_list[input_pointer]
		#### table[top_sym][next_input]=',TD'                 ## Testing purpose
		if top_sym.isupper():
			if table[top_sym][next_input]=='Null':
				valid = 0
				break;
			else:
				tmp_list_2 = []
				char = ''
				length = len(table[top_sym][next_input])
				for i in range(length):
					char_ = table[top_sym][next_input][i]
					char = char + table[top_sym][next_input][i]
					if(char_.isupper()):
						char = ''
						tmp_list_2.append(char_)
					else:
						if char in terminal:
							tmp_list_2.append(char)
							char = ''
				#print(tmp_list_2)
				stack.pop()
				tmp_list_2.reverse()
				for i in tmp_list_2:
					stack.push(i)
				print(stack.print_bottom_up() + "		" + input_string_printer(input_list,input_pointer))
		else:
			if top_sym == input_list[input_pointer]:
				stack.pop()
				input_pointer = input_pointer + 1
				print(stack.print_bottom_up() + "		" + input_string_printer(input_list,input_pointer))
			else:
				valid = 0
				break
	if input_pointer != len(input_list)-1:
		valid = 0
	if valid == 1:
		print("\nHurray String ACCEPTED!!!!")
	else:
		print("\nOh no, String REJECTED!!!!")
