path = " /FileStore/tables/ecommerce_data-6.xls"
try:
    files = dbutils.fs.ls(path)
    print("Directory exists")
except Exception as e:
    if 'java.io.FileNotFoundException' in str(e):
        print("Directory does not exist")


from pyspark.sql import SparkSession
from pyspark.sql.functions import column, sum

spark = SparkSession.builder.appName("LoadCSVExample").getOrCreate()
file_location = "/FileStore/tables/ecommerce_data-7.xls"
df = spark.read.format("com.crealytics.spark.excel") \
  .option("useHeader", "true") \
    .option("header", "true") \
      .option("treatEmptyValuesAsNulls", "true") \
        .option("inferSchema", "true") \
          .load(file_location)


df = df.withColumnRenamed("Transaction ID", "transaction_id") \
       .withColumnRenamed("Product ID", "product_id") \
       .withColumnRenamed("Product Category", "product_category") \
       .withColumnRenamed("Product Subcategory", "product_subcategory") \
       .withColumnRenamed("Product Price", "product_price") \
       .withColumnRenamed("Quantity Sold", "quantity_sold") \
       .withColumnRenamed("Transaction Date", "transaction_date") \
       .withColumnRenamed("Customer ID", "customer_id") \
       .withColumnRenamed("Customer Location", "customer_location") \
       .withColumnRenamed("Payment Method", "payment_method")  

df = df.withColumn("total_sales", col("product_price") * col("quantity_sold"))

total_sales_per_category = df.groupBy("product_category").agg(sum(col("product_price") * col("quantity_sold")).alias("Total Sales"))

# Customer segmentation based on total spend
customer_segmentation = df.groupBy("customer_id").agg(sum(col("product_price") * col("quantity_sold")).alias("Total Spend"))

display(total_sales_per_category)

# Create a view or table

temp_table_name = "ecommerce"

df.createOrReplaceTempView(temp_table_name)

%sql

/* Query the created temp table in a SQL cell */

select * from ecommerce

spark.sql("""
CREATE TABLE IF NOT EXISTS ecommerce_data (
    Transaction_ID INT,
    Product_ID INT,
    Product_Category STRING,
    Product_Subcategory STRING,
    Product_Price FLOAT,
    Quantity_Sold INT,
    Transaction_Date DATE,
    Customer_ID INT,
    Customer_Location STRING,
    Payment_Method STRING,
    Total_Sales FLOAT,
    Transaction_Month INT
)
""")

spark.sql("""
INSERT INTO ecommerce_data
SELECT 
    Transaction_ID,
    Product_ID,
    Product_Category,
    Product_Subcategory,
    Product_Price,
    Quantity_Sold,
    Transaction_Date,
    Customer_ID,
    Customer_Location,
    Payment_Method,
    (Product_Price * Quantity_Sold) AS Total_Sales,
    MONTH(Transaction_Date) AS Transaction_Month
FROM ecommerce
""")

%sql
select Product_Category, Product_Subcategory,sum(Total_Sales) from ecommerce_data group by Product_Category,Product_Subcategory  order by sum(Total_Sales) desc 

%sql
select Product_Category, sum(Total_Sales) from ecommerce_data group by Product_Category order by sum(Total_Sales) desc 