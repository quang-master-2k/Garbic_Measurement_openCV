CREATE TABLE FinalResult (
    MeasureDate VARCHAR(255),
    MeasureTime VARCHAR(255),
    Garment_Style VARCHAR(255),
    Pattern_Code VARCHAR(255),
    Piece_Name VARCHAR(255),
    Size INT,
    Number_checking INT,
    Accepted INT,
    Not_Accepted INT,
    FinalResult VARCHAR(255)
)

Insert into FinalResult (MeasureDate, MeasureTime ,Garment_Style, Pattern_Code, Piece_Name, Size, Number_checking, Accepted, Not_Accepted, FinalResult)
VALUES ('Oct 11th, 2023', '10:05:36', 'A', 'B', 'c', 6, 30, 28, 2, 1)