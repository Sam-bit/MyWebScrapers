BEGIN TRANSACTION;
DROP TABLE IF EXISTS "articles";
CREATE TABLE IF NOT EXISTS "articles" (
	"article_url"	TEXT NOT NULL,
	"article_title"	TEXT NOT NULL,
	"article_thumbnail"	TEXT,
	"article_date"	REAL,
	"article_subtitle"	REAL,
	"article_content"	TEXT NOT NULL,
	"article_checked_by"	TEXT,
	"article_verdict"	TEXT,
	"article_alt_verdict"	TEXT,
	"article_site_id"	INTEGER,
	"article_is_pushed"	INTEGER
);
DROP TABLE IF EXISTS "sources";
CREATE TABLE IF NOT EXISTS "sources" (
	"src_id"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"src_name"	TEXT NOT NULL,
	"src_alt_name"	TEXT,
	"src_logo"	TEXT,
	"src_is_ifcn_approved"	INTEGER,
	"src_address"	TEXT,
	"src_is_active"	INTEGER DEFAULT 1,
	"src_country"	TEXT,
	"src_supported_by"	TEXT,
	"src_language"	TEXT,
	"src_added_date"	TEXT DEFAULT (datetime('now','localtime'))
);
COMMIT;
