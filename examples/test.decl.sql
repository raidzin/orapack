CREATE OR REPLACE PACKAGE utils AS

    FUNCTION get_response(
        request_id IN number
    ) RETURN varchar2;

    FUNCTION get_comment(
        request_id IN number
    ) RETURN varchar2;

    FUNCTION get_question(
        request_id IN number
    ) RETURN varchar2;

END;