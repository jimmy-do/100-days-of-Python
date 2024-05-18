from prettytable import PrettyTable

table = PrettyTable()

# table.field_names = ['Pokémon','Type']
# table.add_row(['Pikachu','Electric'])
# table.add_row(['Squirtle','Water'])
# table.add_row(['Charmander','Fire'])
# print(table)

table.add_column('Pokémon', ['Pikachu', 'Squirtle', 'Charmander'])
table.add_column('Type', ['Electric', 'Water', 'Fire'])
print(table)
