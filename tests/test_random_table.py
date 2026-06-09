# test load table function
import random_table as rt

def test_column_names():

    #arrange

    data_path ="data/example-table.csv"
    expected_output = ['Wheather', 'Time of day', 'Environment', 'Environmental hazard', 'NPCs'] 
    #act
    table = rt.load_table(filepath=data_path)
    output = table.columns.to_list()

    #assert
    assert output == expected_output
    
    pass


def test_categories():

    # arrange
    data_path ="data/example-table.csv"
    expected_output = ['Wheather', 'Time of day', 'Environment', 'Environmental hazard', 'NPCs'] 

    #act
    actual_output = rt.categories(filepath=data_path)

    #assert

    assert actual_output ==expected_output