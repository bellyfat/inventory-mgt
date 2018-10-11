###In it's current state, this program will compare the quantity column for each part in one csv file with another.  

_Right now it will simply show the quantities where the master list has less than supply list._  


- The default filenames that program accepts are:  
   - "Inventory.csv" for the _supply list_  
   - "InvMaster.csv" for the _master list_   
- _You can set your own filenames but you must specify their name and location in command line arguments_
   - _See how to use command line arguments below_


- Both csv files must have the following columns:  

   | VenCode | PartNumber | TotalQty |  
   | ------- |:----------:|:--------:|  


_There is currently no error handling.  
Play nice.  
Use proper csv files with proper columns._

---------------------

__To run this program in command line...__

First, make sure you __[download and install python](https://www.python.org)__ if you haven't already.  

 
- with the default filenames  
   _Place your csv files into the same directory as query.py_   
   _and rename them "SupplyInventory.csv" and "MasterInventory.csv"_  

	```
	python3 query.py
	```  
	
- with __custom filenames__ or paths using __command line arguments__  

   ```
   python3 query.py supply-list-name.csv master-list-name.csv
   ```
