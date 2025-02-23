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
        # self.placeholder_data     = None
        self.form_data              = None
        self.query_handler          = SqlHandler()
        self.template_id:int        = template_id
        # self.types                = None
   
    def __update_placesholders_into_database(self) -> None:
        """
        Processes and updates placeholder types in the database.
        """
        qry = QueryPlaceholders.PLACEHOLDER_UPDATE_TYPE
        for key, value in self.form_data.items():
            if key.startswith('placeholder_'):
                placeholder_id = key.split("_")[1]
                self.query_handler.update_query(qry, value, placeholder_id)


    def fetch_all_placeholders(self, template_id:int) -> list:
        """
        Fetch all placeholders for a given template
        """
        qry = QueryPlaceholders.PLACEHOLDER_SELECT
        if template_id is not None:
            self.template_id = template_id
        
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
        
        qry = None
        return rows
    
    
    # def process_placeholders(self, placeholder_data, types)->None:
    def process_placeholders(self, template_id, form_data)->None:
        """
        Processes and updates placeholder types in the database.
        :param template_id: The ID of the selected template.
        :param form_data: The submitted form data containing placeholder types.
        """
        self.template_id    = template_id
        self.form_data      = form_data
        self.__update_placesholders_into_database()

    

