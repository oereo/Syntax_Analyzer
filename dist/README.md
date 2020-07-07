# Syntax Analyzer

## Goal
 - The goal of the this term-project is to implement a bottom-up syntax analyzer (a.k.a., parser) 
 - Implement the syntax analyzer with the following context free grammar G(CFG)

## CFG
-  Terminals (20) 
1.   vtype for the types of variables and functions 
2.   num for signed integers 
3.   float for floating-point numbers 
4.   literal for literal strings 
5.   id for the identifiers of variables and functions 
6.   if, else, while, for and return for if, else, while, for and return statements respectively 
7.   addsub for + and - arithmetic operators 
8.   multdiv for * and / arithmetic operators 
9.   assign for assignment operators 
10. comp for comparison operators 
11. semi and comma for semicolons and commas respectively 
12. lparen, rparen, lbrace, and rbrace for (, ), {, and } respectively


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

