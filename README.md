# Plex Persist
Plex Persist will take the music meta data from your Plex Server (artist name, track title, album, cover art, etc.) and update the files on your hard disk with that same information. 

#### System Requirements
* Python 3 and Pip installed
* User access to Plex server

#### Dependency Setup
You will need to install the following packages:
* [Plex API](https://github.com/pkkid/python-plexapi) `pip3 install plexapi`
* [Python Magic](https://github.com/ahupp/python-magic) `pip3 install python-magic`
* [Mutagen](https://github.com/quodlibet/mutagen) `pip3 install mutagen`
* [Pillow](https://github.com/python-pillow/Pillow) `pip3 install pillow`

## How To Use
Plex Persist is a python program, executed from the `plex-persist.py` file. It is strongly recommended to create backup, or LVM snapshot, of your data before executing.

#### Running
Run the `plex-persist.py` file with Python 3, adding positional arguments for your server name, section, username and password. Execute the command `python3 plex-persist.py --help` for more information on running.

#### Artist Filtering
The optional `--artist-filter '<name>'` flag allows running only against artists who match the given search criteria. Note that this is not a strict match, nor case sensitive. For instance both the artist 'Mac Miller' and 'Macklemore' will match the flag `--artist-filter 'mac'`.  Additonally, the search results are based on Plex's search algorithm and the results of identical queries are subject to change at any point. **It is strongly recommended you use the `--dry-run` flag when attempting to filter to make sure no additional results are pulled in.**

#### Known Issues
* Plex Persist cannot currently handle `.m4a` files.

## About
Plex Persist aims at persisting the music metadata that is auto-discovered by Plex.

#### Problem
Plex is a very powerful, (mostly) open-source media server. One of it's most impressive functions is the ability to automatically and intelligently look up metadata for your music library, and allow the user to add or correct this data as needed. However, this data is self-contained to the Plex server itself. 

Unfortunately, the Plex team has made it clear that they **will not** include this functionality in the server - they stick to a strict code of "don't change the data," for better or for worse. However, there are many people who wish this was not the case. 
* [Let Plex write the metadata to the file](https://forums.plex.tv/t/let-plex-write-the-metadata-to-the-file/9845)
* [Is there a way to automatically write metadata to media files?](https://www.reddit.com/r/PleX/comments/69sfje/is_there_a_way_to_automatically_write_metadata_to/)
* [Can I take Plex metadata and attach it to files?](https://www.reddit.com/r/PleX/comments/2dc4qv/can_i_take_plex_metadata_and_attach_it_to_files/)
* [Any way to provide metadata outside of the Plex database?](https://www.reddit.com/r/PleX/comments/5ksyfh/any_way_to_provide_metadata_outside_of_the_plex/)
* [Saving Metadata to local files](https://www.reddit.com/r/PleX/comments/2yar8h/saving_metadata_to_local_files/)
* [Is there a way to 'save' metadata I've put in myself for Home Videos that can't be fetched from the internet?](https://www.reddit.com/r/PleX/comments/7z3aj6/is_there_a_way_to_save_metadata_ive_put_in_myself/)
* The list goes on...and on...and on. But you get the point.

#### Existing Solutions
There are a number of solutions that automatically attach metadata to files. But none of these fit the needs I wanted. Most did not integrate with Plex. Some integrated with Plex, but only did metadata for MP4 files in your video library. Some did music, but were limited by only working on certain operating systems.

