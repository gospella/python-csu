CREATE TABLE sentiment_analysis (
    id int AUTO_INCREMENT,
    comment VARCHAR(1000) NOT NULL,
    result VARCHAR(20) NOT NULL,
    created DATETIME DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
);

ALTER TABLE sentiment_analysis
CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;