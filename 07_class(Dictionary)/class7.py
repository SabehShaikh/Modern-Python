from typing import Dict, Union, Optional
import pprint

Key = Union[int,str] # create custom type
Value = Union[int,str,list,dict,tuple,set]

# List      key,value                             
data : Dict[Key, Value] = {
    "fname":"Aslam" ,
    "name": "Qasim" , 
    "education": "MSDS"}

pprint.pprint(data)