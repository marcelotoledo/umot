CREATE SEQUENCE seq_website;
GRANT ALL ON seq_website to umot;

CREATE TABLE website (
       id_website integer      PRIMARY KEY DEFAULT nextval('seq_website'),
       website    varchar(500) NOT NULL
);
GRANT ALL ON website to umot;

CREATE SEQUENCE seq_link;
GRANT ALL ON seq_link to umot;

CREATE TABLE link (
       id_link   integer      PRIMARY KEY DEFAULT nextval('seq_link'),
       id_website integer      NOT NULL REFERENCES website(id_website),
       link       varchar(500) NOT NULL,
       internal   char(1)      DEFAULT 'Y' CHECK (internal in ('Y', 'N')),
       processed  char(1)      DEFAULT 'N' CHECK (processed in ('Y', 'N')),
       updated_at timestamp    DEFAULT current_timestamp,
       created_at timestamp    DEFAULT current_timestamp
);
GRANT ALL ON link to umot;
