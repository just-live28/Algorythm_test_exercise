SELECT dr_name,
       dr_id,
       mcdp_cd,
       Date_format(hire_ymd, '%Y-%m-%d') HIRE_YMD
FROM   doctor
WHERE  mcdp_cd IN ( 'CS', 'GS' )
ORDER  BY hire_ymd DESC,
          dr_name ASC 