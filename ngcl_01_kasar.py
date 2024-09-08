# Non-Graded Challanges 1 (Phase 0 Week 1 Day 2)

# Task #1

# Assigning a List
customer_id = ['B818', 'A461', 'A092', 'A082', 'B341', 'A005', 'A092', 'A461',
               'B219', 'B904', 'A901', 'A083', 'B904', 'A092', 'B341', 'B821',
               'B341', 'B821', 'B904', 'B818', 'A901', 'A083', 'B818', 'A082',
               'B219', 'B219', 'A083', 'A901', 'A082', 'B341', 'B341', 'A083',
               'A082', 'B219', 'B439', 'A461', 'A005', 'A901', 'B341', 'A082',
               'A083', 'A461', 'A083', 'A901', 'A461', 'A083', 'A082', 'A083',
               'B341', 'A901', 'A082', 'A461', 'B219', 'A083', 'B818', 'B821',
               'A092', 'B341', 'A461', 'A092', 'A083', 'B821', 'A092']

# Showing non-duplicate customer_id from customer_id list
non_duplicate_customer_id = set(customer_id)
# Showing number of non-duplicate customer_id from customer_id list
len_non_duplicate_customer_id = len(non_duplicate_customer_id)
print('Number of non-duplicate customer_id from customer_id list is {}'.format(len_non_duplicate_customer_id))

# Task #2

# Assigning a List
Data = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Showing value of 16 from Data List using Indexing
print(Data[3])
# Showing list of [36, 49, 64, 81] from Data List using Indexing
print(Data[5:9])
# Showing list of [100, 81, 64, 49, 36, 25, 16, 9, 4, 1] from Data List using Indexing
print(Data[::-1])

# Task #3

# Assigning a Dictionary with the Keys from Province's Name and the Value from the City's Name
provinsi = {'Nanggroe Aceh Darussalam': 'Aceh',
            'Sumatera Selatan': 'Palembang',
            'Kalimantan Barat': 'Pontianak',
            'Jawa Timur': 'Madiun',
            'Sulawesi Selatan': 'Makassar',
            'Maluku': 'Ambon'}

# Presenting all of the Keys from provinsi Dictionary into a list
print('List of Keys in provinsi Dictionary:')
print(list(provinsi.keys()))
# Changing the value of 'Jawa Timur' Key from 'Madiun' into 'Surabaya' in provinsi Dictionary
print('The Value of Jawa Timur Key Before the Change is',provinsi['Jawa Timur'])
provinsi['Jawa Timur'] = 'Surabaya'
print('The Value of Jawa Timur Key After the Change is', provinsi['Jawa Timur'])