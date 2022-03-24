#-------------------------#
# Title: Assignment08.py
# Desc.: Working with classes and functions, and OOP
# Change Log: (Who, When, What)
# <GByron, 2022-Mar-23 Edited, added, and adjusted code>
#-------------------------#

# -- DATA -- #
strFileName = 'cdInventory.txt'
lstOfCDObjects = []

class CD:
    """Stores data about a CD:

    properties:
        cdID: (int) with CD ID
        cdTitle: (string) with the title of the CD
        cdArtist: (string) with the artist of the CD
    methods:

    """
    #-Fields-#
        # N/A
    #-Constructor-#
    def __init__(self, cdID, cdTitle, cdArtist):
    #-Attributes-#
        self.cdID = cdID
        self.cdTitle = cdTitle
        self.cdArtist = cdArtist
        
    def cdID(self):
        return self.cdID
    
    def cdTitle(self):
        return self.cdTitle
    
    def cdArtist(self):
        return self.cdArtist
    
    """Function to add CD to table
    
    Args:
        None
        
    Returns:
        None
        
    """
    
    def adding_cd():
        cd_lst= IO.add_cd()
        dicRow = {'ID': cd_lst[0], 'Title': cd_lst[1], 'Artist': cd_lst[2]}
        lstOfCDObjects.append(dicRow)
    

# -- PROCESSING -- #
class FileIO:
    """Processes data to and from file:

    properties:

    methods:
        save_inventory(file_name, lst_Inventory): -> None
        load_inventory(file_name): -> (a list of CD objects)

    """
    
    """Processing the data to and from text file"""
    
    @staticmethod
    def read_file(file_name, table):
        
        """Function to manage data ingestion from file to a list of dictionaries

        Reads the data from file identified by file_name into a 2D table
        (list of dicts) table one line in the file represents one dictionary row in table.

        Args:
            file_name (string): name of file used to read the data from
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime

        Returns:
            None.
        """
        
        try:
            open('CDInventory.txt')
        except FileNotFoundError:
            input('The inventory was NOT read. The file was not found.')
        table.clear()
        objFile = open(file_name, 'r')
        for line in objFile:
            data = line.strip().split(',')
            dicRow = {'ID': int(data[0]), 'Title': data[1], 'Artist': data[2]}
            table.append(dicRow)
        objFile.close()
        
    def save_data(data, strFileName):
        
        """"Function to save the CD to a file
        
        Args:
            file_name: the name of the file the CD information will be saved to
            table: the list of the CD information that will be saved
            
        Returns:
            None
            
        """
        
        if strYesNo == 'y':
            objFile = open(strFileName, 'w')
            for row in lstOfCDObjects:
                lstValues = list(row.values())
                lstValues[0] = str(lstValues[0])
                objFile.write(','.join(lstValues) + '\n')
            objFile.close()
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')

# -- PRESENTATION (Input/Output) -- #

class IO:
   
    """Handling Input / Output"""

    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """

        print('Menu\n\n[l] Load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[s] Save Inventory to file\n[x] Exit\n')
    
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, d, s or x

        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, s or x]: ').lower().strip()
        print() 
        return choice
    
    @staticmethod
    def show_inventory(table):
        """Displays current inventory table


        Args:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        Returns:
            None.

        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in table:
            print('{}\t{} (by:{})'.format(*row.values()))
        print('======================================')
        
        
        """Adds CD of user choice to the list, does not save the CD to memory
        
        Args: None
        
        Returns:
            strID, asks user for deired value to identity ID
            strTitle, asks user for title of CD associated with ID
            strArtist, asks user for CD artist
        
        """
        
    def add_cd():
        while True:
            strID = input('Enter ID: ').strip()
            try:
                intID = int(strID)
                break
            except ValueError:
                print('That is not an integer!')
        strTitle = input('Enter the CD\'s title. ').strip()
        stArtist = input('Enter the Artist\'s name. ').strip()
        return [intID, strTitle, stArtist]

# -- Main Body of Script -- #

try:
    FileIO.read_file(strFileName, lstOfCDObjects)
    
finally:
    while True:
        
        IO.print_menu()
        strChoice = IO.menu_choice()

        # let user exit program
        if strChoice == 'x':
            break
    
        # let user load inventory from file
        if strChoice == 'l':
            print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
            strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled')
            if strYesNo.lower() == 'yes':
                print('reloading...')
                FileIO.read_file(strFileName, lstOfCDObjects)
                IO.show_inventory(lstOfCDObjects)
            else:
                input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
                IO.show_inventory(lstOfCDObjects)
                continue

        # let user add data to the inventory
        elif strChoice == 'a':
             CD.adding_cd()
             IO.show_inventory(lstOfCDObjects)
             continue  
     
        # show user current inventory
        elif strChoice == 'i':
             IO.show_inventory(lstOfCDObjects)
             continue  
     
        # let user save inventory to file
        elif strChoice == 's':
            try:
                open('CDInventory.txt')
            except FileNotFoundError:
                input('The inventory was NOT saved to file. The file was not found.')
                print('File has been created!')
            IO.show_inventory(lstOfCDObjects)
            strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
            FileIO.save_data(lstOfCDObjects, strFileName)
            continue
         
    else:
         print('General Error')





