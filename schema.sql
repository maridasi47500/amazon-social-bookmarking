create table if not exists user(
        id integer primary key autoincrement,
        username text,
            email text,
            password text,
            phone text,
            country_id text
                    );
create table if not exists country(
        id integer primary key autoincrement,
        name text
                    );
create table if not exists cat(
        id integer primary key autoincrement,
        name text
                    );
create table if not exists photo(
        id integer primary key autoincrement,
        country_id text,
            cat_id text,
            pic text
                    );
create table if not exists songs(
        id integer primary key autoincrement,
        country_id text,
            title text,
            artist text,
            music text
                    );
create table if not exists likes(
        id integer primary key autoincrement,
        user_id text,
            photo_id text
                    );
create table if not exists likesongs(
        id integer primary key autoincrement,
        user_id text,
            song_id text
                    );
