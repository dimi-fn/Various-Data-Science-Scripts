-- round 

SELECT round(107.088, 2) from dual


SELECT round(107.088, 3) from dual


SELECT round(107.0887, 3) from dual


SELECT round(107.9) from dual

-- trunc 

SELECT trunc(107.938439849) from dual


SELECT trunc(107.938439849, 3) from dual


SELECT trunc(107.938439849, 5) from dual

-- sysdate 

SELECT sysdate from dual

-- systimestamp 

SELECT systimestamp from dual

-- add_months 

SELECT add_months('11/17/2012', 3)
from dual


SELECT add_months('11/17/2012', -3)
from dual


SELECT add_months(sysdate, -3)
from dual


SELECT add_months(sysdate, +100)
from dual

-- months_between 

SELECT months_between('12/15/2012', '12/4/2013')
from dual


SELECT months_between('12/4/2013', '12/15/2012')
from dual


SELECT months_between('12/4/2013', '12/4/2012')
from dual


SELECT trunc(systimestamp) from dual


SELECT trunc(systimestamp, 'YEAR') from dual


SELECT trunc(systimestamp, 'MONTH') from dual


SELECT hiredate, trunc(hiredate, 'MONTH') from emp


SELECT ename, hiredate, trunc(hiredate, 'MONTH') from emp


SELECT ename, hiredate, trunc(hiredate, 'MONTH')
from emp
where trunc(hiredate, 'YEAR') = '01/01/1982'

