-- dbt model: staging_uber_trips
{{ config(materialized='table') }}

select 
    vendor_id,
    pickup_datetime,
    dropoff_datetime,
    passenger_count,
    trip_distance,
    fare_amount,
    -- Add more columns from parquet
from {{ source('uber_raw', 'trips') }}

{{ dbt_utils.date_spine(
    datepart="hour",
    start_date="2023-01-01",
    end_date="2023-12-31"
) }}