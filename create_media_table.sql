CREATE TABLE IF NOT EXISTS hoyj.media
(
        title String,
	speaker_fname String,
	speaker_lname String,
	topic String,
	book String,
	chapter Int,
	s_verse Int,
	e_verse Int,
	dt Date,
        part_num Int,
	file_type String,
	file_location String,
	url_location String,
        notes_url String,
        notes_file_location String
) ENGINE = MergeTree()
ORDER BY dt
