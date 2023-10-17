CREATE TABLE MeasuredResult (
    MeasureDate VARCHAR(255),
    MeasureTime VARCHAR(255),
    Garment_Style VARCHAR(255),
    Pattern_Code VARCHAR(255),
    Piece_Name VARCHAR(255),
    Size INT,
    Dimension_Name VARCHAR(255),
    Dimension_Value FLOAT,
    Dimension_Result BIT,
    Comparison_Edge VARCHAR(255),
    Error_Distance FLOAT,
    Max_Distance Float
)

Insert into MeasuredResult (MeasureDate, MeasureTime ,Garment_Style, Pattern_Code, Piece_Name, Size, Dimension_Name, Dimension_Value, Dimension_Result, Comparison_Edge, Error_Distance, Max_Distance)
VALUES ('Oct 11th, 2023', '10:02:59', 'A', 'B', 'c', 6, 'L8/AC954CBKF-3', 15.29, 1, 5, 5.6, 5.6)