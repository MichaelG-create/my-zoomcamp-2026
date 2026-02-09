SELECT COUNT(*) FROM `dtc-de-course-484720.zoomcamp.yellow_tripdata` 
WHERE TIMESTAMP_TRUNC(lpep_pickup_datetime, MONTH) = TIMESTAMP("2021-03-01")