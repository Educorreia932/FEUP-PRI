DROP TABLE IF EXISTS album CASCADE;
DROP TABLE IF EXISTS album CASCADE;
DROP TABLE IF EXISTS album CASCADE;
DROP TABLE IF EXISTS album CASCADE;
DROP TABLE IF EXISTS album CASCADE;

DROP TABLE IF EXISTS album CASCADE;
DROP TABLE IF EXISTS album CASCADE;
DROP TABLE IF EXISTS album CASCADE;
DROP TABLE IF EXISTS album CASCADE;
DROP TABLE IF EXISTS album CASCADE;
DROP TABLE IF EXISTS album CASCADE;

DROP TYPE IF EXISTS albumType

CREATE TYPE albumType AS ENUM ('album', 'single', 'compilation');

CREATE TABLE Album{
	id SERIAL PRIMARY KEY,
	type albumType,
	total_tracks INTEGER NOT NULL CONSTRAINT total_tracks > 0, --Make equal to number of objects?
	--dunno if we should include images, I ignored them here
	name text NOT NULL,
	release_date date, --not null?
	uri text --not null?
	album_id text NOT NULL
};

CREATE TABLE Track{
	id SERIAL PRIMARY KEY,
	explicit BOOLEAN DEFAULT FALSE,
	duration_ms INTEGER,
	track_id text NOT NULL,
	lyrics_id INTEGER REFERENCES Lyrics(id)
};

CREATE TABLE TrackPosition{
	track_id INTEGER NOT NULL REFERENCES Track(id),
	album_id INTEGER NOT NULL REFERENCES Album(id),
	track_position INTEGER NOT NULL,
	PRIMARY KEY (track_id, album_id)
};

CREATE TABLE Artist{

};

CREATE TABLE Genre{

};

CREATE TABLE Lyrics{
	id SERIAL PRIMARY_KEY,
	lyrics TEXT NOT NULL,
	track_id REFERENCES Track(id)
};