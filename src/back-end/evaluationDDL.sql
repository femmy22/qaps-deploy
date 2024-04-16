DROP TABLE IF EXISTS test;
DROP TABLE IF EXISTS rawData;
DROP TABLE IF EXISTS score;
DROP TABLE IF EXISTS measurement;
DROP PROCEDURE IF EXISTS calculate_scores;

CREATE TABLE rawData(
    sessionID VARCHAR(255),
    shape VARCHAR(255),
    x_cords MEDIUMTEXT,
    y_cords MEDIUMTEXT,
    time_stamps MEDIUMTEXT,
    x_canvas_dimension DOUBLE,
    y_canvas_dimension DOUBLE
);

CREATE TABLE test(
    sessionID VARCHAR(255),
    shape VARCHAR(255),
    dimension VARCHAR(255),
    score DOUBLE(5,3)
);

CREATE TABLE score(
    sessionID VARCHAR(255),
    straightness DOUBLE(5,3),
    equilaterality DOUBLE(5,3),
    alignment DOUBLE(5,3),
    roundness DOUBLE(5,3),
    closure DOUBLE(5,3),
    spacing DOUBLE(5,3),
    lineRatio DOUBLE(5,3),
    bisection DOUBLE(5,3),
    bisectionAngle DOUBLE(5,3),
    score DOUBLE(5,3),
    PRIMARY KEY(sessionID)
);

CREATE TABLE measurement(
    sessionID VARCHAR(255),
    shape VARCHAR(255),
    dimension VARCHAR(255),
    score DOUBLE(22,10)
);

-- use: cursor.callproc('calculate_scores',['session id']) 
CREATE PROCEDURE calculate_scores(
    IN input_sessionID VARCHAR(50)
)
BEGIN   
    DECLARE calculated_avg DOUBLE;
    DECLARE final_score DOUBLE;

    -- insert initial values for all dimensions
    INSERT INTO score (sessionID, straightness, equilaterality, alignment, roundness, closure, spacing, lineRatio, bisection, bisectionAngle)
    VALUES (input_sessionID, -1, -1, -1, -1, -1, -1, -1, -1, -1);

    -- [straightness] calculate average in test table and update score table value for corresponding dimension
    SELECT AVG(score) INTO calculated_avg FROM test WHERE dimension = 'straightness' AND sessionID = input_sessionID;
    UPDATE score SET straightness = calculated_avg WHERE sessionID = input_sessionID;

    -- [equilaterality] calculate average in test table and update score table value for corresponding dimension
    SELECT AVG(score) INTO calculated_avg FROM test WHERE dimension = 'equilaterality' AND sessionID = input_sessionID;
    UPDATE score SET equilaterality = calculated_avg WHERE sessionID = input_sessionID;

    -- [alignment] calculate average in test table and update score table value for corresponding dimension
    SELECT AVG(score) INTO calculated_avg FROM test WHERE dimension = 'alignment' AND sessionID = input_sessionID;
    UPDATE score SET alignment = calculated_avg WHERE sessionID = input_sessionID;

    -- [roundness] calculate average in test table and update score table value for corresponding dimension
    SELECT AVG(score) INTO calculated_avg FROM test WHERE dimension = 'roundness' AND sessionID = input_sessionID;
    UPDATE score SET roundness = calculated_avg WHERE sessionID = input_sessionID;

    -- [closure] calculate average in test table and update score table value for corresponding dimension
    SELECT AVG(score) INTO calculated_avg FROM test WHERE dimension = 'closure' AND sessionID = input_sessionID;
    UPDATE score SET closure = calculated_avg WHERE sessionID = input_sessionID;

    -- [spacing] calculate average in test table and update score table value for corresponding dimension
    SELECT AVG(score) INTO calculated_avg FROM test WHERE dimension = 'spacing' AND sessionID = input_sessionID;
    UPDATE score SET spacing = calculated_avg WHERE sessionID = input_sessionID;

    -- [lineRatio] calculate average in test table and update score table value for corresponding dimension
    SELECT AVG(score) INTO calculated_avg FROM test WHERE dimension = 'lineRatio' AND sessionID = input_sessionID;
    UPDATE score SET lineRatio = calculated_avg WHERE sessionID = input_sessionID;

    -- [bisection] calculate average in test table and update score table value for corresponding dimension
    SELECT AVG(score) INTO calculated_avg FROM test WHERE dimension = 'bisection' AND sessionID = input_sessionID;
    UPDATE score SET bisection = calculated_avg WHERE sessionID = input_sessionID;

    -- [bisectionAngle] calculate average in test table and update score table value for corresponding dimension
    SELECT AVG(score) INTO calculated_avg FROM test WHERE dimension = 'bisectionAngle' AND sessionID = input_sessionID;
    UPDATE score SET bisectionAngle = calculated_avg WHERE sessionID = input_sessionID;

    -- calculate final score for given sessionID
    SELECT (SUM(straightness) + SUM(equilaterality) + SUM(alignment) + SUM(roundness) + SUM(closure) + SUM(spacing) + SUM(lineRatio) + SUM(bisection) + SUM(bisectionAngle)) INTO final_score 
    FROM score 
    WHERE sessionID = input_sessionID;

    -- update score table with calculated final score value
    UPDATE score SET score = final_score WHERE sessionID = input_sessionID;

END;
