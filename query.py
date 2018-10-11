from csv import DictReader
import sys


if len(sys.argv) > 2:
    filename_master = sys.argv[1]
    filename_supply = sys.argv[2]
else:
    filename_master = 'MasterInventory.csv'
    filename_supply = 'SupplyInventory.csv'

print("Master filename:", filename_master)
print("Supply filename:", filename_supply)

def get_value_set(dictionary, key):
    """Accepts a list of dictionaries and a key string.
    Returns a set off all the values at keys with the value of key string. 
    """
    value_set = set()
    for id in dictionary:
        value_set.add(dictionary.get(id).get('VenCode'))
    return value_set


def build_dict_from_csv(filename, filter_row=None):
    """Builds dictionary from csv file.
    CSV file must include columns: VenCode,PartNumber,TotalQty
    """
    if not filename.endswith('.csv'):
        print("This is not a proper csv file.")
        return False

    dictionary = {}
    with open(filename, newline='') as file:
        reader = DictReader(file) 
        for row in reader:
            if filter_row == None or not filter_row(row):

                id = f'{row.get("VenCode")}-{row.get("PartNumber")}'
                details = {
                    'VenCode': row.get('VenCode'),
                    'TotalQty': row.get('TotalQty'),
                }
                dictionary[id] = details
    return dictionary


def create_filter(keep_set):
    """Returns a function that has access to outer parameter of keep_set.
    The returned function will return True if a row is not in the keep_set.
    """
    def filter_row(row):
        return True if row.get('VenCode') not in keep_set else False
    return filter_row


def update_master_qty():
    master_dict = build_dict_from_csv(filename_master)

    ven_codes = get_value_set(master_dict, 'VenCode')

    filter_cb = create_filter(ven_codes)

    _supply_dict = build_dict_from_csv(filename_supply, filter_cb)
    
    for part_id in master_dict:
        master_qty = master_dict[part_id]['TotalQty']
        supply_qty = _supply_dict[part_id]['TotalQty']
        if master_qty < supply_qty:
            print("master:", 
                master_qty, 
                "supply:", 
                supply_qty
            )

update_master_qty()
