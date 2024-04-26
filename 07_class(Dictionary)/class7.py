from typing import Dict, TypedDict , Union, Optional, Tuple
import pprint

Key = Union[int,str] # create custom type
Value = Union[int,str,list,dict,tuple,set]

# List      key,value                             
data : Dict[Key, Value] = {
    "fname":"Aslam" ,
    "name": "Qasim" , 
    "education": "MSDS"}

pprint.pprint(data)

# from typing import Dict, Union, Optional
# import pprint

# mydata2: TypedDict("data2", {"a": str,"b":str})
# Key = Union[int,str] # create custom type
# Value = Union[int, str, list, data2, Tuple, set]

# # List                    0                1            2
# data : Dict[Key,Value] = {
#                         "fname":"Muhammad Aslam",
#                         "name":"Muhammad Qasim",
#                         "education": "MSDS",
#                         "abc" : [1,2,3, "abc"],
#                         'xyz': {1,2,3},
#                         'efg' : (1,2,3),
#                         'cde' : {"a":1, "b":2},
#                         'items': [[1, 2, 3], [4, 5, 6], {7, 8, 9}],
#                         # [1,2,3] : "Pakistan", # error
#                         # {1,2,3} : "pakistan", #error
#                         }

# print(data["cde"]['b'])
# print(data["abc"])
# print(data["items"])