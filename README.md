# Syntax Analyzer

## Goal
 - The goal of the this term-project is to implement a bottom-up syntax analyzer (a.k.a., parser) 
 - Implement the syntax analyzer with the following context free grammar G(CFG)

## CFG
1. Terminals (20) 
  *   vtype for the types of variables and functions 
  *   num for signed integers 
  *   float for floating-point numbers 
  *   literal for literal strings 
  *   id for the identifiers of variables and functions 
  *   if, else, while, for and return for if, else, while, for and return statements respectively 
  *   addsub for + and - arithmetic operators 
  *   multdiv for * and / arithmetic operators 
  *   assign for assignment operators 
  *   comp for comparison operators 
  *   semi and comma for semicolons and commas respectively 
  *   lparen, rparen, lbrace, and rbrace for (, ), {, and } respectively


- Non-terminals (14) 
CODE, VDECL, FDECL, ARG, MOREARGS, BLOCK, STMT, ASSIGN, RHS, EXPR, TERM, FACTOR, COND, RETURN


- Start symbol: CODE


## STEP

1. To construct an NFA for recognizing viable prefixes of G
2. To convert the NFA into a DFA
3. To compute the follow sets
4. To construct a SLR parsing table
5. To implement a SLR parser 

## EXECUTION

- Input : An output of lexical analyzer program
- Output : just an acceptance message(if output is *'rejected'* make an error report which explains why and where the error occurred)

## HOW

1. https://www.python.org/downloads/ - Download Python

2. Install xlrd library to handle EXEL file data
```
  $ pip install xlrd  
```

3. Install pyinstaller to create EXE file
```
  $ pip install pyinstaller  
```

4. Create the EXE file
```
  $ pyinstaller --onefile syntax_analyzer.py 
```

5. Copy the dist/syntax_analyzer.exe in current directory
```
  $ cd dist
  $ copy syntax_analyzer.exe ..
```

6. Execute the syntax_analyzer.exe
```
  $ syntax_analyzer.exe lexical_output.txt
```