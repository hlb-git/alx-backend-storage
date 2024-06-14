-- sql query to calculate the year band group have been in existence or the year they splited

SELECT band_name, (IFNULL(split, 2022) - formed) AS lifespan
    FROM metal_bands
    WHERE style LIKE '%Glam rock%'
    ORDER BY lifespan DESC;
