#!/usr/bin/env python
# encoding: utf-8
# author: Glad Ma Zekun
import pymysql.cursors

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='QQpp1111',
                             db='test',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


# save commit
def insert_comment(music_id, comments, detail, connection0):
    with connection0.cursor() as cursor:
        sql = "INSERT INTO 'comments' ('MUSIC_ID', 'COMMENTS', 'DETAILS') VALUES (%S, %S, %S)"
        cursor.execute(sql, (music_id, comments, detail))
    connection0.commit()
    cursor.close()


# save music
def insert_music(music_id, music_name, album_id):
    with connection.cursor() as cursor:
        sql = "INSERT INTO 'musics' ('MUSIC_ID', 'MUSIC_NAME', 'ALBUM_ID') VALUES (%S, %S, %S)"
        cursor.execute(sql, (music_id, music_name, album_id))
    connection.commit()
    cursor.close()


# save album
def insert_album(album_id, artist_id):
    with connection.cursor() as cursor:
        sql = "INSERT INTO 'ablbums' ('ALBUM_ID', 'ARTIST_ID') VALUES (%S, %S)"
        cursor.execute(sql, (album_id, artist_id))
    connection.commit()
    cursor.close()


# save artists
def insert_artist(artist_id, artist_name):
    with connection.cursor() as cursor:
        sql = "INSERT INTO 'artists' ('ARTIST_ID', 'ARTIST_NAME') VALUES (%S, %S)"
        cursor.execute(sql, (artist_id, artist_name))
    connection.commit()
    cursor.close()


# get all artist
def get_all_artist():
    with connection.cursor() as cursor:
        sql = "SELECT `ARTIST_ID` FROM `artists` ORDER BY ARTIST_ID"
        cursor.execute(sql, ())
        return cursor.fetchall()


# get all album
def get_all_album():
    with connection.cursor() as cursor:
        sql = "SELECT `ALBUM_ID` FROM `albums` ORDER BY ALBUM_ID"
        cursor.execute(sql, ())
        return cursor.fetchall()


# get all music
def get_all_music():
    with connection.cursor() as cursor:
        sql = "SELECT 'MUSIC_ID' FROM 'musics' ORDER_BY MUSIC_ID"
        cursor.execute(sql, ())
        return cursor.fetchall()


# get before_music
def get_before_music():
    with connection.cursor() as cursor:
        sql = "SELECT `MUSIC_ID` FROM `musics` ORDER BY MUSIC_ID LIMIT 0, 800000"
        cursor.execute(sql, ())
        return cursor.fetchall()


# get after music
def get_after_music():
    with connection.cursor() as cursor:
        sql = "SELECT `MUSIC_ID` FROM `musics` ORDER BY MUSIC_ID LIMIT 800000, 1197429"
        cursor.execute(sql, ())
        return cursor.fetchall()


# dis connect
def dis_connect():
    connection.close()
