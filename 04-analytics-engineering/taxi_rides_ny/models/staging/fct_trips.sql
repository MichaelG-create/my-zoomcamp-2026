/* 
To do: 
- one row per trip (doesn't matter green or yellow)
- Add a primary key column 'trip_id'. It has to be unique across both green and yellow taxis.
- Find all the duplicates based on the combination of vendor_id, pickup_datetime, dropoff_datetime, and passenger_count.
- Filter out duplicates keeping only one record per trip based on the above combination. (understatand why duplicates exist?)
- Fix them
- Find a way to enrich the column payment_type to have consistent meaning across both green and yellow taxis.
*/

select 
  1 as trip_id  -- placeholder for trip_id column
from {{ ref('int_trips') }}