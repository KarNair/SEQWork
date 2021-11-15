## sequence.py ##


# This file contains a class declaration.
# I have included the initializer and an example method to help you.
# You will need to add the other methods yourself.


class Sequence:

	""" This method is the initializer, it is called when creating (instantiating) an object (instance) of this class. 
	This __init__ method has been modified the input case insensitive """

	def __init__(self, bases):

		# store the bases as an attribute.
		self.bases = bases.upper()



	# TODO: add other methods here to complete the tasks.

	def first_base(self):

	    """We can access the 'bases' for this instance via 'self'. 
	    This is an example method, it returns the first base."""

	    result = self.bases[0]
	    return result


	def base_count(self):

		""" Returns number of bases in the input sequence object """

		base_counter = len(self.bases)

		return(base_counter)


	def is_dna(self):

		""" Checks whether the input sequence is DNA"""

		if self.base_count() == 0:

			return(False)

		else:

			dna_base = "ATGC"
			check_dna = all(i in dna_base for i in self.bases)

			return(check_dna)



	def comp_seq(self):

		""" Generates complementary sequence for the input sequence """

		assert self.is_dna() == True, "Sequence Error. The input sequence is not DNA"

		comp_base = str.maketrans("ATGC","TACG")
		comp_dna = self.bases.translate(comp_base)
		comp_dna = Sequence(comp_dna)


		return(comp_dna)



	def non_match_base(self,other):
		
		""" Returns first non-matching base index """


		seq1 = self.bases
		seq2 = other.bases


		assert len(seq1) == len(seq2), "Comparison Error. Cannot compare sequences of different lengths"


		for base_pair in range(0, len(seq1)):

			if seq1[base_pair] != seq2[base_pair]:

				return(base_pair)
				break


		else:


			return(-1)