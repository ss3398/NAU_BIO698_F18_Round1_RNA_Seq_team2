use bio698;

create table k_table ( 
id integer,
target_id varchar(1000),
sample varchar(1000),
est_counts decimal(50,10),
tpm decimal(50,10),
eff_len integer,
len decimal(10),
resistance_profile varchar(100),
treatment varchar(100)
);

