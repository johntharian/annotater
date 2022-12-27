from fastapi import FastAPI

app = FastAPI()


# data={
#   "query":["meds","food","car"],
#   "product":[[
#     {"name": "omega",
#       "description":"1 for each meal"
#     }
#   ],
#     [
#     {"name": "bananna",
#       "description":"3 in 1"
#     }
#   ],
#  [
#     {"name": "honda",
#       "description":"best for city drive"
#     }
#   ]
#   ]
# }

# def remove_pair_from_buffer():
    


def get_item_from_buffer():
    return {
        "query":"car",
        "product":{"name": "honda",
                    "description":"best for city drive"
                    },
        "annotated":0
            }

@app.get("/annotate")
def anotate():
    data=get_item_from_buffer()
    print(f"query = {data['query']}")
    print(f"product = {data['product']['name']} , {data['product']['description']}")
    
    print("1 - perfect match","2 - somwhat relevent","3 - not relevent")
    
    a= input()
    
    remove_from_db_1(data)
    data['annotated']=a
    save_to_db_2(data)
    
    
    