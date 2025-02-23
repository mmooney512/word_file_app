# /query / placeholder.py

class QueryPlaceholders():
    # version
    PLACEHOLDER_INSERT ="""
        INSERT INTO placeholder
        (template_id, placeholder_name, placeholder_order)

        SELECT	?, ?, ?

        EXCEPT

        SELECT template_id, placeholder_name, placeholder_order
        FROM placeholder
        WHERE template_id = ?
        AND placeholder_name = ?
        AND deleted = 0
        ;
        """
    
    PLACEHOLDER_SELECT ="""
        SELECT placeholder_id,
                template_id,
                placeholder_type,
                placeholder_name
        FROM placeholder
        WHERE template_id = ?
        AND deleted = 0
        ORDER BY placeholder_order
        ;
        """
    
    PLACEHOLDER_UPDATE_TYPE ="""
        UPDATE placeholder
        SET placeholder_type = ?
        WHERE template_id = ? 
        AND placeholder_name = ?
        AND deleted = 0
        ;
        """
    