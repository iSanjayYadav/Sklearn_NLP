CREATE TABLE pages(
    page_id INTEGER PRIMARY KEY,
    page_title TEXT,
    page_text TEXT
);

CREATE TABLE category (
	category_id INTEGER PRIMARY KEY,
	category_title TEXT
);


CREATE TABLE page_category(
	page_category_id SERIAL PRIMARY KEY,
	category_id INTEGER,
	page_id INTEGER  
);
