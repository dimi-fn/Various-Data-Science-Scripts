SELECT to_char(sysdate, 'mm-dd-yyyy') from dual


SELECT to_char(sysdate, 'mm/dd/yyyy') from dual


SELECT to_char(sysdate, 'dd-mm-yyyy') from dual


SELECT to_char(sysdate, 'ddth "of" month, yyyy') from dual

-- Solution to assignment at 10:52 

SELECT ename, sal, to_char(sal, '$99,999.99') salaries from emp

-- to_date function 

SELECT to_date('2012-08-27', 'yyyy-mm-dd'))
from dual


SELECT add_months(to_date('2012-08-27', 'yyyy-mm-dd'), 2)
from dual


SELECT to_date('3 of June, 2012', 'dd "of" Month, YYYY')
from dual

