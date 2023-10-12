CREATE TABLE ComparisonDatabase(
    Garment_Style VARCHAR(255),
    Pattern_Code VARCHAR(255),
    Piece_Name VARCHAR(255),
    Num_Corners INT,
    Tolerance FLOAT,
    Hard_patternImg VARCHAR(255)
)

SELECT * FROM ComparisonDatabase

Insert into ComparisonDatabase (Garment_Style, Pattern_Code, Piece_Name, Num_Corners, Tolerance, Hard_patternImg)
VALUES ('A', 'B', 'C', 6, 1/4, 'hardpart.jpg')