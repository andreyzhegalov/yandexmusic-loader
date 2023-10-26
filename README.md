
# Описание

Скрипт для скачивания треков с yandex music.
Позволяет скачивать:

* трек отдельно
* альбом
* треки из favourite списка
* playlist

Работатет на основе библиотеки [yandex-music](https://yandex-music.readthedocs.io/en/main/).

# Использование

Перед запуском установить переменную окружения `TOKEN` со значением `access_token` yandex music.
Создать папку `result` в директории скрипта для результатов скачивания.

## Варианты запуска

* Скачивание трека по идентификатору `track_id`. Идентификатор можно получить из url запрооса в DevTools

``` bash
python main.py playlist --track {track_id}

```

* Скачивание альбома по идентификатору `album_id`. Идентификатор можно получить из url запрооса в DevTools

``` bash
python main.py playlist --album {album_id}

```

* Скачивание треков из favourite списка. Список берется для установленного `TOKEN`

``` bash
python main.py favourite

```

* Скачивание playlist с имененем `playlist_name`. Можно использовать только назания плейлистов данного пользователя (определяется по `TOKEN`).

``` bash
python main.py playlist --title {playlist_name}

```
