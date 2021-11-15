import unittest
import sequence
from sequence import Sequence as sq
#from sequence import non_match_base




class TestSequence(unittest.TestCase):


	def setUp(self):
		self.sequence_normal =  sq("ATGCTTAG")
		self.sequence_complimentary = sq("TACGAATC")
		self.sequence_normal2 = sq("ATGCATAG")
		self.sequence_diff_length = sq("ATGGG")
		self.sequence_single_base = sq("C")
		self.sequence_empty = sq("")
		self.sequence_not_dna = sq("ThisIsNotDNA")
		self.sequence_rna = sq("AUGGCGC")
		self.sequence_number = sq("4485")
		self.sequence_special_character = sq("$!##!%$^%#^!%$#^!%#$!$#!^")
		self.sequence_whitespace = sq(" ")


	# Test base_count()
	def test_base_count(self):

		self.assertEqual(self.sequence_normal.base_count(),8)    #Test sequence length
		self.assertEqual(self.sequence_single_base.base_count(), 1)     #Test sequence length for single base
		self.assertEqual(self.sequence_empty.base_count(), 0)     #Test empty sequence


	# Test is_dna()
	def test_is_dna(self):

		self.assertEqual(self.sequence_normal.is_dna(),True)   #Test DNA validity for regular DNA sequence
		self.assertEqual(self.sequence_single_base.is_dna(), True)   #Test DNA validity for single base
		self.assertEqual(self.sequence_empty.is_dna(), False)   #Test DNA validity for empty sequence
		self.assertEqual(self.sequence_not_dna.is_dna(), False)   #Test DNA validity for non-DNA sequence
		self.assertEqual(self.sequence_rna.is_dna(), False)    #Test DNA validity for RNA sequence
		self.assertEqual(self.sequence_number.is_dna(), False)   #Test DNA validity for Numeric sequence
		self.assertEqual(self.sequence_special_character.is_dna(), False)    #Test DNA validity for special character sequence
		self.assertEqual(self.sequence_whitespace.is_dna(), False)    #Test DNA validity for whitespace sequence


	# Test comp_seq()
	def test_comp_seq(self):

		self.assertEqual(self.sequence_normal.comp_seq().bases,self.sequence_complimentary.bases)   #Test comp_seq() output against manually defined complimentary sequence of sequence_normal
		self.assertRaises(Exception, sq.comp_seq, self.sequence_not_dna)    #Check that exception is raised when one of the sequence is not DNA
		self.assertRaises(Exception, sq.comp_seq, self.sequence_empty)   #Check that exception is raised when one of the sequence is empty
		self.assertIsInstance(self.sequence_normal.comp_seq(), sq, "This object is not a Sequence class instance")    #Check if the complimentary sequence is an instance of Sequence class.



	#Test non_match_base()
	def test_non_match_base(self):

		self.assertEqual(self.sequence_normal.non_match_base(self.sequence_normal2), 4)   #Check zero-index of first non matching base for sequences of equal length. 
		self.assertEqual(self.sequence_normal.non_match_base(self.sequence_normal), -1)   #Check that output is -1 when sequences are identical
		self.assertEqual(self.sequence_empty.non_match_base(self.sequence_empty), -1)    #Check that output is -1 when both sequences are empty
		self.assertRaises(Exception, sq.non_match_base, self.sequence_normal, self.sequence_diff_length)    #Check that exception is raised when sequences are of different lengths





if __name__ == '__main__':
	unittest.main()
