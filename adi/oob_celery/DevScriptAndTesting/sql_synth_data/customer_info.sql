--- function for random  int (so will use based number of customer in customer-in)

CREATE OR REPLACE FUNCTION random_between(low INT ,high INT) 
   RETURNS INT AS
$$
BEGIN
   RETURN floor(random()* (high-low + 1) + low);
END;
$$ language 'plpgsql' STRICT;


CREATE TABLE customer_info(
   info_id SERIAL PRIMARY KEY,
   company_id INT,
   contact_name VARCHAR(255) NOT NULL,
   phone VARCHAR(25),
   email VARCHAR(100),
	customer_id  int ,
   CONSTRAINT fk_customer_info
      FOREIGN KEY(customer_id) 
      REFERENCES customer(customer_id)
);


delete from customer_info





drop table customer_binary;
CREATE TABLE customer_binary(
   data_id SERIAL PRIMARY KEY,
   customer_bin_data BYTEA,
	customer_id  int ,
   CONSTRAINT fk_customer_data
      FOREIGN KEY(customer_id) 
      REFERENCES customer(customer_id)
);



create extension pgcrypto;

INSERT INTO customer_binary(data_id, customer_bin_data, customer_id)
SELECT id, gen_random_bytes(16), cust FROM generate_series(1,100000) id ,random_between(1,599) cust;   





select * from customer_info


INSERT INTO customer_info(info_id, contact_name, phone, email,customer_id)
SELECT id, md5(random()::text), md5(random()::text)::varchar(20), md5(random()::text) ,cust
FROM generate_series(1,10000) id ,random_between(1,599) cust;


update customer_info
   set customer_id = floor(random_between(1,599));




   

drop table customer_binary;
CREATE TABLE customer_binary(
   data_id SERIAL PRIMARY KEY,
   customer_bin_data BYTEA,
	customer_id  int ,
   CONSTRAINT fk_customer_data
      FOREIGN KEY(customer_id) 
      REFERENCES customer(customer_id)
);



create extension pgcrypto;

INSERT INTO customer_binary(data_id, customer_bin_data, customer_id)
SELECT id, gen_random_bytes(16), cust FROM generate_series(1,1000000) id ,random_between(1,599) cust;   


update customer_binary
   set customer_id = floor(random_between(1,599));

select distinct(customer_id ), count(customer_id) from customer_binary  group by customer_id  
having count(customer_id) >1 