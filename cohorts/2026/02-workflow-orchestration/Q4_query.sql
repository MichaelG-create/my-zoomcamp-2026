SELECT COUNT(*) FROM `dtc-de-course-484720.zoomcamp.green_tripdata` 
WHERE TIMESTAMP_TRUNC(lpep_pickup_datetime, YEAR) = TIMESTAMP("2020-01-01");