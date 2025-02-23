# /src/document_handler.py

# system library -------------------------------------------------------------
import io

# packages -------------------------------------------------------------------
import docx

# local library --------------------------------------------------------------
from src.sql_handler            import SqlHandler
from query.document_template    import QueryDocumentTemplate
from query.placeholder          import QueryPlaceholders

class WebFormHandler():
    def __init__(self, template_id):
        self.template_id:int                = template_id
        self.placeholder_data               = None
        self.query_handler                  = SqlHandler()
        self.types                          = None

    
    def __insert_placesholders_into_database(self) -> None:
        """
        Inserts placeholders for the template into the database
        """
        qry = QueryPlaceholders.PLACEHOLDER_UPDATE_TYPE

        # insert the file into the database
        for self.placeholder_data, self.types in zip(self.placeholder_data, self.types):
            self.query_handler.update_query(qry, self.types, self.template_id, self.placeholder_data)
        qry = None
       
    def fetch_all_placeholders(self) -> list:
        """
        Fetch all placeholders for a given template
        """
        qry = QueryPlaceholders.PLACEHOLDER_SELECT

        # insert the file into the database
        rows = self.query_handler.select_query(user_query=qry, params=[self.template_id])

        qry = None

        return rows
    
    def fetch_all_templates(self) -> list:
        """
        Fetch list of all the templates
        """
        qry = QueryDocumentTemplate.DOCUMENT_SELECT_ALL
        rows = self.query_handler.select_query(user_query=qry)

        return rows
    
    
    def process_placeholders(self, placeholder_data, types)->None:
        """
        Process the placeholders from the web form
        """
        self.placeholder_data               = placeholder_data
        self.types                          = types
        self.__insert_placesholders_into_database()

    

