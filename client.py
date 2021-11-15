## client.py ##
import sequence


# Create an instance of the Sequence class.
example_sequence1 = sequence.Sequence('AGCTAGATAGCCATGATGCC')
example_sequence2 = sequence.Sequence('AGCCTGTCATGTCTAAATTG')
#example_not_sequence = sequence.Sequence("ThisIsATest")



# Call the first_base method on our instance.
example_first_base = example_sequence1.first_base()
print(f'The first base is: {example_first_base}')

print("\n")

# TODO add method calls to complete the tasks



# base_count method call
seq_len = example_sequence1.base_count()
print("Length of the sequence is: ", seq_len)
print("\n")



#is_dna method call
check_dna = example_sequence1.is_dna()

if check_dna == True:
	print("This is a valid DNA sequence")
	print("\n")
else:
	print("Invalid DNA sequence")
	print("\n")



#comp_seq method call
comp_seq = example_sequence1.comp_seq()

print("The object type of complimentary sequence is: ",comp_seq)
print("The complimentary sequence is: ", comp_seq.bases)
print("\n")



#non_match method call
non_match_index = example_sequence1.non_match_base(example_sequence2)

print("The zero-based index of first non matching base is:", non_match_index)