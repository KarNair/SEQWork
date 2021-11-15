## client.py ##
import sequence


# Create an instance of the Sequence class.
example_sequence1 = sequence.Sequence('AGCTAGATAGCCATGATGCC')
example_sequence2 = sequence.Sequence('AGCCTGTCATGTCTAAATTG')
example_not_sequence = sequence.Sequence("NotASequence")



# Call the first_base method on our instance.
example_first_base = example_sequence1.first_base()
print(f'The first base is: {example_first_base}')


# TODO add method calls to complete the tasks


# base_count() METHOD CALL
seq_len = example_sequence1.base_count()
print("Length of the sequence is:", seq_len)


#is_dna() METHOD CALL
check_dna = example_sequence1.is_dna()
#check_dna = example_not_sequence.is_dna()    # UNCOMMENT TO CHECK INVALID SEQUENCE
if check_dna == True:
	print("The input sequence is a valid DNA sequence")
else:
	print("Invalid DNA sequence")


# comp_seq() METHOD CALL
comp_seq = example_sequence1.comp_seq()

print("The complimentary sequence of",example_sequence1.bases,"is:", comp_seq.bases)
print("The object class of complimentary sequence is:",type(comp_seq))


#non_match_base() METHOD CALL
non_match_index = example_sequence1.non_match_base(example_sequence2)
print("The zero-based index of first non matching base is:", non_match_index)


## UNCOMMENT LINES BELOW TO CHECK non_match_base FOR IDENTICAL SEQUENCE
#non_match_index_clone = example_sequence1.non_match_base(example_sequence1)
#print("The zero-based index of first non matching base is:", non_match_index_clone)