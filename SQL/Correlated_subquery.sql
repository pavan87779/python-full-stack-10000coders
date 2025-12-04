#WAQTD: Name of employee and his manager name if employee is working as CLERK
SELECT e.ename AS emp_name,
       (SELECT m.ename FROM emp m WHERE m.empno = e.mgr) AS manager_name
FROM emp e
WHERE e.job = 'CLERK';

#WAQTD: Name of the emp and manager designation if manager works in dept 10 or 20
SELECT e.ename AS emp_name,
       (SELECT m.job FROM emp m 
        WHERE m.empno = e.mgr AND m.deptno IN (10,20)
       ) AS manager_job
FROM emp e;

#WAQTD: Name of employee and manager’s salary if emp and manager both earn more than 2300
SELECT e.ename AS emp_name,
       (SELECT m.sal FROM emp m WHERE m.empno = e.mgr) AS manager_sal
FROM emp e
WHERE e.sal > 2300
  AND EXISTS (
      SELECT 1 FROM emp m WHERE m.empno = e.mgr AND m.sal > 2300
  );

#WAQTD: ENAME and MANAGER HIREDATE if employee was hired before 1982
SELECT e.ename AS emp_name,
       (SELECT m.hiredate FROM emp m WHERE m.empno = e.mgr) AS manager_hiredate
FROM emp e
WHERE e.hiredate < DATE '1982-01-01';

#WAQTD: EMP details and DEPARTMENT details
SELECT e.*, d.deptno, d.dname, d.loc
FROM emp e
JOIN dept d ON e.deptno = d.deptno;


#WAQTD: Names of emps along with deptno and loc of emps. (Do it with all possible joins)
SELECT e.ename, e.deptno, d.loc
FROM emp e
JOIN dept d ON e.deptno = d.deptno;

#WAQTD: Names along with the dnames of emps (do it with all possible joins
SELECT e.ename, d.dname
FROM emp e
JOIN dept d ON e.deptno = d.deptno;

#8) WAQTD: ENAME, SAL along with the DEPT details of emps who are earning SAL > 1500
SELECT e.ename, e.sal, d.deptno, d.dname, d.loc
FROM emp e
JOIN dept d ON e.deptno = d.deptno
WHERE e.sal > 1500;

#9) WAQTD: ENAME, DNAME, SAL of all the employees if their salary is greater than 2340
SELECT e.ename, d.dname, e.sal
FROM emp e
LEFT JOIN dept d ON e.deptno = d.deptno
WHERE e.sal > 2340;

#10) WAQTD: DNAME, JOB of emps whose job and dname start with character 'S'

SELECT DISTINCT d.dname, e.job
FROM emp e
JOIN dept d ON e.deptno = d.deptno
WHERE e.job LIKE 'S%' AND d.dname LIKE 'S%';
