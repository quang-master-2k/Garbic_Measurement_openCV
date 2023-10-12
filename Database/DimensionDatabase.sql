CREATE TABLE DimensionDatabase (
    Garment_Style VARCHAR(255),
    Pattern_Code VARCHAR(255),
    Piece_Name VARCHAR(255),
    Num_Corners INT,
    Size INT,
    Dimension_Name VARCHAR(255),
    Dimension_Value FLOAT
)

SELECT * FROM DimensionDatabase
DELETE FROM DimensionDatabase

Insert into DimensionDatabase (Garment_Style, Pattern_Code, Piece_Name, Num_Corners, Size, Dimension_Name, Dimension_Value)
VALUES ('A', 'B', 'C', 6, 13, 'L8/AC954CBKF-3', 15.29)