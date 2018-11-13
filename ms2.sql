use bio698;

create table k_table_summary as
select target_id
,AVG(case when substr(sample,locate('_S',sample,length(sample)-5)+1) in ('S1','S2','S3') then est_counts else 0 end) s1
,AVG(case when substr(sample,locate('_S',sample,length(sample)-5)+1) in ('S7','S10','S8') then est_counts else 0 end) s2
,AVG(case when substr(sample,locate('_S',sample,length(sample)-5)+1) in ('S11','S9','S12') then est_counts else 0 end) s3
,AVG(case when substr(sample,locate('_S',sample,length(sample)-5)+1) in ('S4','S5','S6') then est_counts else 0 end) s4
,STDDEV(case when substr(sample,locate('_S',sample,length(sample)-5)+1) in ('S1','S2','S3') then est_counts else 0 end) sd1
,STDDEV(case when substr(sample,locate('_S',sample,length(sample)-5)+1) in ('S7','S10','S8') then est_counts else 0 end) sd2
,STDDEV(case when substr(sample,locate('_S',sample,length(sample)-5)+1) in ('S11','S9','S12') then est_counts else 0 end) sd3
,STDDEV(case when substr(sample,locate('_S',sample,length(sample)-5)+1) in ('S4','S5','S6') then est_counts else 0 end) sd4
from k_table 
group by target_id;

create table k_s_table as
select t1.target_id,t1.s1,t1.s2,t1.s3,t1.s4,t1.sd1,t1.sd2,t1.sd3,t1.sd4,ifnull(t2.pval,0) pval, ifnull(t2.qval,0) qval, ifnull(t2.sigma_sq,0) sigma_sq
from k_table_summary t1 left outer join S_TABLE t2 
on (t1.target_id = t2.target_id);

select 'target_id','s1','s2','s3','s4','sd1','sd2','sd3','sd4','pval','qval','sigma_sq' 
union all
select * 
into outfile '/var/lib/mysql-files/Output.txt' fields terminated by ',' optionally enclosed by '"' lines terminated by '\n' 
from k_s_table;

select 'target_id','sample','est_counts'
union all
select target_id,
(case substr(sample,locate('_S',sample,length(sample)-5)+1) 
when 'S1' then 'Sample 1' 
when 'S2' then 'Sample 1' 
when 'S3' then 'Sample 1' 
when 'S7' then 'Sample 2' 
when 'S10' then 'Sample 2' 
when 'S8' then 'Sample 2' 
when 'S11' then 'Sample 3' 
when 'S9' then 'Sample 3'
when 'S12' then 'Sample 3' 
else 'Sample 4' end) sample,
est_counts 
into outfile '/var/lib/mysql-files/readcounts.txt' fields terminated by ',' lines terminated by '\n' 
from k_table where target_id in (select target_id from S_TABLE where pval = (select min(pval) from S_TABLE));


