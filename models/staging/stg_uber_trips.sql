{{ config(materialized='table') }}

select
    VendorID as vendor_id,
    tpep_pickup_datetime as pickup_datetime,
    tpep_dropoff_datetime as dropoff_datetime,
    passenger_count,
    trip_distance,
    RatecodeID as rate_code_id,
    PULocationID as pickup_location_id,
    DOLocationID as dropoff_location_id,
    payment_type,
    fare_amount,
    extra,
    mta_tax,
    tip_amount,
    tolls_amount,
    improvement_surcharge,
    total_amount,
    congestion_surcharge,
    airport_fee
from {{ source('raw', 'RAW_UBER_TRIPS') }}
where pickup_datetime is not null
  and dropoff_datetime is not null
  and total_amount > 0