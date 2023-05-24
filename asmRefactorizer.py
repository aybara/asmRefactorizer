#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, re

registers = {
    'rax' : [r'\brax\b', r'\beax\b', r'\bax\b', r'\bal'],
    'rbx' : [r'\brbx\b', r'\bebx\b', r'\bbx\b', r'\bbl'],
    'rcx' : [r'\brcx\b', r'\becx\b', r'\bcx\b', r'\bcl'],
    'rdx' : [r'\brdx\b', r'\bedx\b', r'\bdx\b', r'\bdl'],
    'r8': [r'\br8\b', r'\br8d\b', r'\br8w\b', r'\br8b'],
    'r9' : [r'\br9\b', r'\br9d\b', r'\br9w\b', r'\br9b'],
    'r10' : [r'\br10\b', r'\br10d\b', r'\br10w\b', r'\br10b'],
    'r11' : [r'\br11\b', r'\br11d\b', r'\br11w\b', r'\br11b'],
    'r12' : [r'\br12\b', r'\br12d\b', r'\br12w\b', r'\br12b'],
    'r13' : [r'\br13\b', r'\br13d\b', r'\br13w\b', r'\br13b'],
    'r14' : [r'\br14\b', r'\br14d\b', r'\br14w\b', r'\br14b'],
    'r15' : [r'\br15\b', r'\br15d\b', r'\br15w\b', r'\br15b'],
    'rsi' : [r'\brsi\b', r'\besi\b', r'\bsi\b', r'\bsil'],
    'rdi' : [r'\brdi\b', r'\bedi\b', r'\bdi\b', r'\bdil']
}    

replacements = {
    'rax' : [' rax', ' eax', ' ax', ' al'],
    'rbx' : [' rbx', ' ebx', ' bx', ' bl'],
    'rcx' : [' rcx', ' ecx', ' cx', ' cl'],
    'rdx' : [' rdx', ' edx', ' dx', ' dl'],
    'r8': [' r8', ' r8d', ' r8w', ' r8b'],
    'r9' : [' r9', ' r9d', ' r9w', ' r9b'],
    'r10' : [' r10', ' r10d', ' r10w', ' r10b'],
    'r11' : [' r11', ' r11d', ' r11w', ' r11b'],
    'r12' : [' r12', ' r12d', ' r12w', ' r12b'],
    'r13' : [' r13', ' r13d', ' r13w', ' r13b'],
    'r14' : [' r14', ' r14d', ' r14w', ' r14b'],
    'r15' : [' r15', ' r15d', ' r15w', ' r15b'],
    'rsi' : [' rsi', ' esi', ' si', ' sil'],
    'rdi' : [' rdi', ' edi', ' di', ' dil']
}   

def replaceRegisters(text, currentRegister, newRegister):
    finalText = text
    for i in range(0, len(registers[currentRegister])):
        finalText = re.sub(registers[currentRegister][i], replacements[newRegister][i], finalText)  
        #finalText.replace(registers[currentRegister][i], replacements[newRegister][i])
    return finalText

def __main__():
    if len(sys.argv) < 4:
        print('Usage: python3 file [register1 registerReplacement1 register2 registerReplacement2... ]')
        return 1

    file = sys.argv[1]
    inFile = open(file, 'r')
    text = inFile.read()

    for i in range(2, len(sys.argv), 2):
        currentRegister = sys.argv[i]
        newRegister = sys.argv[i+1]
        if((currentRegister == 'rax' or currentRegister == 'rdx') and ('div' in text or 'mul' in text)):
            print('You are trying to replace rax or rdx register with div or mul operator in the code!!!')
            return 1

        text = replaceRegisters(text, currentRegister, newRegister)
    print(text)
    
    return 0

__main__()


