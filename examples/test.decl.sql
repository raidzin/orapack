CREATE OR REPLACE PACKAGE emp_actions AS
TYPE emprectyp IS RECORD (emp_id INT, salary REAL);
CURSOR desc_salary RETURN EMPRECTYP;
PROCEDURE hire_employee(
    ename VARCHAR2,
    job VARCHAR2,
    mgr NUMBER,
    sal NUMBER,
    comm NUMBER,
    deptno NUMBER
);
PROCEDURE fire_employee(emp_id NUMBER);
END emp_actions;
