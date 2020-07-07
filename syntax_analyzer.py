import xlrd
import sys

def read_lexical_output(filepath):
	f = open(filepath, 'r')
	f.close()

def read_cell(sheet, row, col):
	return sheet.cell_value(row - 1, col - 1)

def get_symbols_from_lexical_output(lexical_file_path):
	symbols = []
	# read lexical_output.txt to get symbols
	lexical_output_start_string = "- Output: "
	lexical_output_start_string_len = len(lexical_output_start_string)

	lexical_output_file = open(lexical_file_path, 'r')
	line = lexical_output_file.readline()
	while line:
		if line.startswith(lexical_output_start_string):
			# remove "\n"
			line = line[:-1]
			# get symbols ex) <type, value> 
			line = line[lexical_output_start_string_len:]
			# get symbols and save 
			while line.find('<') >= 0:
				# remove '<'
				start = line.find('<')
				line = line[start + 1:]

				if line[0].isalpha() == False:
					continue

				# <type> or <type,value>
				end = 0
				comma_idx = line.find(',')
				end_idx = line.find('>')

				if end_idx < comma_idx:
					end = end_idx
				else:
					end = comma_idx

				# save symbol type in symbol list
				symbol_type = line[:end]
				symbols.append(symbol_type)
		
		line = lexical_output_file.readline()
	# close lexical_output.txt
	lexical_output_file.close()

	return symbols

# must enter lexical_output.txt
if len(sys.argv) != 2:
	print("please enter lexical_output.txt")
	sys.exit()

# read lexical_output.txt and get symbols
symbols = get_symbols_from_lexical_output(sys.argv[1])
print(symbols)

# open excel files
item_number_file = xlrd.open_workbook("Item_Number.xlsx")
reduce_rule_file = xlrd.open_workbook("Reduce_Rule.xlsx")
SLR_ParsingTable_file = xlrd.open_workbook("SLR_ParsingTable.xlsx")

# read sheet from excel file
item_number = item_number_file.sheet_by_name("Sheet1")
reduce_rule = reduce_rule_file.sheet_by_name("Sheet1")
slr_parsingtable = SLR_ParsingTable_file.sheet_by_name("Sheet1")

# init stack, state
stack = []

# set symbols and col num
symbols_type_list = ["", "", "vtype", "num", "float", "literal", "id"
					, "if", "else", "while", "for", "return"
					, "addsub", "multdiv", "assign", "comp", "semi"
					, "comma", "lparen", "rparen", "lbrace", "rbrace"]

# goto symbol list
goto_type_list = ["CODE", "VDECL", "FDECL", "ASSIGN", "ARG"
				, "MOREARGS", "BLOCK", "STMT", "ELSE", "RHS"
				, "EXPR", "TERM", "FACTOR", "COND", "RETURN"]

# first time, push start state into the stack 
stack.append(3)

# Run slr-parsing by using slr-parsingtable.xslx and Reduce_Rule.xslx
while True:
	print("-----------")
	# get current state from stack
	print("stack: ", stack)
	current_state = stack[-1]
	print("current_state: ", current_state)

	# get current state and next input symbol
	next_symbol = symbols[0]
	print("next input symbol: ", next_symbol)

	# search next action from SLR_ParsingTable.xlsx
	next_symbol_column = symbols_type_list.index(next_symbol)
	next_action_cell = read_cell(slr_parsingtable, current_state, next_symbol_column)
	print("next_action: ", next_action_cell)

	action = next_action_cell[:1]

	# push the next state into the stack and move next symbol
	# if action is S, shift and goto next state
	if action == 'S':
		next_state = int(next_action_cell[1:])
		stack.append(next_state)
		symbols = symbols[1:]
	# action is R, reduce by Rules (by using Reduce_Rule.xlsx)
	if action == 'R':
		next_state = int(next_action_cell[2:-1])	
		
		rule = read_cell(reduce_rule, next_state, 2)
		print("Rule: ", rule, "\n")
		
		# get left and right part
		tmp = rule.split(' ')
		left = tmp[0]
		right = tmp[2:]
	
		# pop content from the stack
		pop_cnt = len(right)
		stack = stack[:-pop_cnt]
		print("stack after pop: ", stack)

		# get new current state after pop from the stack
		current_state = stack[-1]
		print("state after pop: ", current_state)

		# get new state from goto table
		goto_action_column = goto_type_list.index(left)
		next_state = read_cell(slr_parsingtable, current_state, goto_action_column + 23)				 
		print("next action in goto table: ", left, current_state)
		
		if next_state is None:
			stack.append(next_state)
		else:	
			next_state = int(next_state)

		# push new state by reduce
			stack.append(next_state)
