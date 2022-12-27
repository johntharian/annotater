def save_data_to_db(db,item):  # saves a query proudct pair to database

def get_data_from_db():   # gets existing query product pair from database
    

def generate_qp(): # generates query product pairs  in a list
    data=get_data_from_openSearch()
    
    test={
    'query' : ['meds','cars'],
    'products' : [{ 'name' : 'omega','description' : 'one for each day'},{ 'name' : 'honda','description' : 'great performance'}],
    'annotated' : [0,0,]
    }
    return test
    
    
def get_data_from_openSearch():  # gets data from open search 
    
    
def check() : # checks if query product pair exists in database
    data=generate_qp()
    
    data_exist=get_data_from_db()
    
    for qp_pair in data_exist:    #checks for qp 
        if qp_pair in data_exist:
            data.pop(qp_pair)
            

def check_for_annotations(qp :dict): # checks if query product are annotated 
    if qp['annotated']!=0:
        data_exist=get_data_from_db()
        data_exist.pop(qp)
        save_data_to_db(db,qp)
        