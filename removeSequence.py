#!/usr/bin/python

###############################################################################
#
#    removeSequence.py version 1.0
#    
#    Removes a specified nucleotide sequence from the beginning of a larger sequence
#
#    Useful for preparing FASTA files for certain processing pipelines that do not
#    allow for distal barcodes or primers
#
#    Copyright (C) 2014 Evan Denmark
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################



import argparse

parser = argparse.ArgumentParser(description = ' ')
parser.add_argument('fasta',help= 'fasta file with adaptor sequences')
parser.add_argument('adaptor_sequence', help= 'string of nucleotides')

fasta = parser.parse_args().fasta
adaptor_sequence = parser.parse_args().adaptor_sequence


def remove_fusion_adaptors(fasta, adaptor_sequence):
	"""
	Removes the fusion adaptor at the beginning of each sequence of a FASTA file
	"""
	fasta = str(fasta)
	old_file = open(fasta, 'r')
	new_file = open('new_'+fasta+'.fasta', 'w')
	length_adaptor = len(adaptor_sequence)	
	for each_line in old_file:
		each_line = str(each_line)
		if each_line[0] == '>':
			#name line
			new_file.write(each_line)
		else:
			#sequence line
			if each_line[:(length_adaptor)] == adaptor_sequence:
				current_line = each_line[:].rstrip('\n').lstrip()
				current_line = str(current_line)
				adaptor_sequence=adaptor_sequence[:length_adaptor]
				new_line = current_line[length_adaptor:]
				new_file.write(new_line+'\n')
				
	old_file.close()
	new_file.close()

remove_fusion_adaptors(fasta, adaptor_sequence)
			
		
			
