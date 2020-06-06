
hash_table = {'item ' + str(i): i for i in range(10)}
print(hash_table)
hash_table['item 10'] = 10
hash_table['item 11'] = 11
print(hash_table)

for key, value in hash_table.items():
    print('Key: ', key, ', ', 'Value: ', value)