CREATE TABLE sentiment_analysis (
    id int AUTO_INCREMENT,
    comment VARCHAR(1000) NOT NULL,
    result VARCHAR(20) NOT NULL,
    created DATETIME DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
);