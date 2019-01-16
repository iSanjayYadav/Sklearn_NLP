CREATE TABLE category (
	cid INTEGER,
	name TEXT,
	PRIMARY KEY (cid));

CREATE TABLE page (
	pid INTEGER,
	title TEXT,
	text TEXT,
	PRIMARY KEY(pid));

CREATE TABLE category_page(
	page_pid INTEGER,
	category_cid INTEGER);	



