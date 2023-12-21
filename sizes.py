    #all_sizes = {'S', 43, 'XL', 40, 44, 'M', 12, 'IT 35', 'IT 43', 'FR 12', 'UK 50', 'XXL', 'IT 50'}
    #ordered_sizes = {'XS': 0,'S': 1, 'M': 2, 'L': 3, 'XL': 4, 'XXL': 5}
    
    #filter all sizes for italian sizes iterating to the all_sizes set and mapping the italian sizes in the ordered_sizes dictionary
    #inside a for cicle:
    #   if the size is an italian size:
    #       map it the following way if the italian is from 30 to 40 is XS if it is from 41 to 45 is S if it is from 46 to 48 is M if it is from 49 to 52 is L if it is from 53 to 56 is XL if it is from 57 to 60 is XXL
    #       add the resulted mapped value to the ordered_sizes dictionary saving the value from the italian size but it's key is mapped from ordered_sizes dictionary for example a size of IT 35 will be assign a vlaue of 0 from the ordered sizes dictionary
    #       remove it from the all_sizes set
    #       add it to the italian_sizes set
    #   else:
    #       pass
    #print the italian_sizes set

    #filter all sizes for number sizes iterating to the all_sizes set and mapping the number sizes in the ordered_sizes dictionary
    #inside a for cicle:
    #   if the size is a number size:
    #       map it the following way if the number is from 30 to 40 is XS if it is from 41 to 45 is S if it is from 46 to 48 is M if it is from 49 to 52 is L if it is from 53 to 56 is XL if it is from 57 to 60 is XXL
    #       add the resulted mapped value to the ordered_sizes dictionary saving the value from the number size but it's key is mapped from ordered_sizes dictionary for example a size of 35 will be assign a vlaue of 0 from the ordered sizes dictionary
    #       remove it from the all_sizes set
    #   else:
    #       pass

""" all_sizes = {'S', 43, 'XL', 40, 44, 'M', 12, 'IT 35', 'IT 43', 'FR 12', 'UK 50', 'XXL', 'IT 50'}
ordered_sizes = {'XS': 0, 'S': 1, 'M': 2, 'L': 3, 'XL': 4, 'XXL': 5, '3XL': 6}

italian_sizes = set()

for size in set(all_sizes):  # Use a copy of all_sizes to iterate over
    mapped_size = None

    if isinstance(size, str) and size.startswith('IT '):
        it_size = int(size.split()[1])
        # Map Italian size to the corresponding category
        if 30 <= it_size <= 40:
            mapped_size = 'XS'
        elif 41 <= it_size <= 45:
            mapped_size = 'S'
        elif 46 <= it_size <= 48:
            mapped_size = 'M'
        elif 49 <= it_size <= 52:
            mapped_size = 'L'
        elif 53 <= it_size <= 56:
            mapped_size = 'XL'
        elif 57 <= it_size <= 60:
            mapped_size = 'XXL'
        if mapped_size:
            ordered_sizes[size] = ordered_sizes[mapped_size]
            italian_sizes.add(size)
            all_sizes.remove(size)

    elif isinstance(size, str) and size.startswith('UK '):
        uk_size = int(size.split()[1])
        if uk_size == 50:  # Example mapping for UK 50
            mapped_size = 'XL'
        if mapped_size:
            ordered_sizes[size] = ordered_sizes[mapped_size]
            all_sizes.remove(size)

    elif isinstance(size, str) and size.startswith('FR '):
        fr_size = int(size.split()[1])
        if fr_size == 12:  # Example mapping for FR 12
            mapped_size = 'L'
        if mapped_size:
            ordered_sizes[size] = ordered_sizes[mapped_size]
            all_sizes.remove(size)

    elif isinstance(size, int):
        # Map the small number size to the corresponding category
        if 1 <= size <= 2:
            mapped_size = 'XS'
        elif 3 <= size <= 4:
            mapped_size = 'S'
        elif 5 <= size <= 6:
            mapped_size = 'M'
        elif 7 <= size <= 8:
            mapped_size = 'L'
        elif 9 <= size <= 10:
            mapped_size = 'XL'
        elif 11 <= size <= 12:
            mapped_size = 'XXL'
        if mapped_size:
            ordered_sizes[size] = ordered_sizes[mapped_size]
            all_sizes.remove(size)

# Sort the dictionary by its values
ordered_sizes_by_value = {k: v for k, v in sorted(ordered_sizes.items(), key=lambda item: item[1])}

print("Italian Sizes:", italian_sizes)
print("Ordered Sizes by Value:", ordered_sizes_by_value)
print("Remaining All Sizes:", all_sizes)
 """

""" def map_size_to_category(size):
    if 30 <= size <= 40:
        return 'XS'
    elif 41 <= size <= 45:
        return 'S'
    elif 46 <= size <= 48:
        return 'M'
    elif 49 <= size <= 52:
        return 'L'
    elif 53 <= size <= 56:
        return 'XL'
    elif 57 <= size <= 60:
        return 'XXL'

all_sizes = {'S', 43, 'XL', 40, 44, 'M', 12, 'IT 35', 'IT 43', 'FR 12', 'UK 50', 'XXL', 'IT 50'}
ordered_sizes = {'XS': 0, 'S': 1, 'M': 2, 'L': 3, 'XL': 4, 'XXL': 5}
italian_sizes = set()
sizes_to_remove = set()

for size in all_sizes:
    if isinstance(size, str) and size.startswith('IT '):
        it_size = int(size.split()[1])
        mapped_size = map_size_to_category(it_size)
        if mapped_size is not None:
            ordered_sizes[size] = ordered_sizes[mapped_size]
            italian_sizes.add(size)
            sizes_to_remove.add(size)
    elif isinstance(size, int):
        mapped_size = map_size_to_category(size)
        if mapped_size is not None:
            ordered_sizes[size] = ordered_sizes[mapped_size]
            sizes_to_remove.add(size)

# Remove processed sizes from all_sizes
all_sizes.difference_update(sizes_to_remove)

# Sort ordered_sizes by value
ordered_sizes_by_value = {k: v for k, v in sorted(ordered_sizes.items(), key=lambda item: item[1])}

print("Italian Sizes:", italian_sizes)
print("Ordered Sizes by Value:", ordered_sizes_by_value)
print("All Sizes:", all_sizes) """

def map_size_to_category(size, size_type):
    if size_type == 'IT' and 30 <= size <= 60:
        return ['XS', 'S', 'M', 'L', 'XL', 'XXL'][(size - 30) // 5]
    elif size_type == 'number' and 35 <= size <= 70:
        return ['XS', 'S', 'M', 'L', 'XL', 'XXL'][(size - 35) // 6]
    elif size_type == 'UK' and 20 <= size <= 55:
        return ['XS', 'S', 'M', 'L', 'XL', 'XXL'][(size - 20) // 6]
    elif size_type == 'FR' and 2 <= size <= 20:
        return ['XS', 'S', 'M', 'L', 'XL', 'XXL'][(size - 2) // 3]
    elif size_type == 'small' and 1 <= size <= 12:
        return ['XS', 'S', 'M', 'L', 'XL', 'XXL'][(size - 1) // 2]

all_sizes = {'S', 43, 'XL', 40, 44, 'M', 12, 'IT 35', 'IT 43', 'FR 12', 'UK 50', 'XXL', 'IT 50'}
ordered_sizes = {'XS': 0, 'S': 1, 'M': 2, 'L': 3, 'XL': 4, 'XXL': 5}
italian_sizes = set()
sizes_to_remove = set()

for size in all_sizes:
    mapped_size = None

    if isinstance(size, str) and size.startswith('IT '):
        it_size = int(size.split()[1])
        mapped_size = map_size_to_category(it_size, 'IT')
        italian_sizes.add(size)
    elif isinstance(size, str) and size.startswith('UK '):
        uk_size = int(size.split()[1])
        mapped_size = map_size_to_category(uk_size, 'UK')
    elif isinstance(size, str) and size.startswith('FR '):
        fr_size = int(size.split()[1])
        mapped_size = map_size_to_category(fr_size, 'FR')
    elif isinstance(size, int):
        mapped_size = map_size_to_category(size, 'number')

    if mapped_size is not None:
        ordered_sizes[size] = ordered_sizes[mapped_size]
        sizes_to_remove.add(size)

# Remove processed sizes from all_sizes
all_sizes.difference_update(sizes_to_remove)

# Sort ordered_sizes by value
ordered_sizes_by_value = {k: v for k, v in sorted(ordered_sizes.items(), key=lambda item: item[1])}

print("Italian Sizes:", italian_sizes)
print("Ordered Sizes by Value:", ordered_sizes_by_value)
print("All Sizes:", all_sizes)

